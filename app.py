import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, make_response, abort
from config import Config
from models import db, Category, Post, ContactMessage

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)

    # Register Context Processors for global SEO & Navigation variables
    @app.context_processor
    def inject_global_seo():
        return {
            'site_name': Config.SITE_NAME,
            'site_url': Config.SITE_BASE_URL,
            'current_year': datetime.now().year,
            'all_categories': Category.query.all()
        }

    # ==========================================
    # ROUTES
    # ==========================================

    @app.route('/')
    def index():
        featured_posts = Post.query.filter_by(is_featured=True).order_by(Post.created_at.desc()).limit(3).all()
        recent_posts = Post.query.order_by(Post.created_at.desc()).limit(6).all()
        categories = Category.query.all()
        
        # SEO Meta tags for Homepage
        page_seo = {
            'title': 'FitPulse | Gen-Z Student Fitness, Healthy Diet & Wellness Guide',
            'description': 'FitPulse is your modern college guide to budget healthy eating, fast dorm workouts, late-night study snacks, and natural student energy. Master your physical and mental game.',
            'keywords': 'healthy diet for college students, student fitness, dorm workouts, cheap meal prep, exam energy, student wellness',
            'canonical': f"{Config.SITE_BASE_URL}/",
            'og_type': 'website',
            'og_image': 'https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=1200&q=80'
        }
        
        return render_template('index.html', 
                               featured_posts=featured_posts, 
                               recent_posts=recent_posts, 
                               categories=categories,
                               seo=page_seo)

    @app.route('/blog')
    def blog_list():
        category_slug = request.args.get('category')
        search_query = request.args.get('q', '').strip()
        
        query = Post.query
        active_category = None
        
        if category_slug:
            active_category = Category.query.filter_by(slug=category_slug).first_or_404()
            query = query.filter_by(category_id=active_category.id)
            
        if search_query:
            query = query.filter(
                (Post.title.ilike(f'%{search_query}%')) | 
                (Post.content.ilike(f'%{search_query}%')) |
                (Post.keywords.ilike(f'%{search_query}%'))
            )
            
        posts = query.order_by(Post.created_at.desc()).all()
        categories = Category.query.all()
        
        # Dynamic SEO for category or archive
        if active_category:
            seo_title = f"{active_category.name} Articles | FitPulse College Wellness"
            seo_desc = f"Explore {active_category.name.lower()} articles on FitPulse. Practical fitness and nutrition guides crafted for college students."
            canonical = f"{Config.SITE_BASE_URL}/blog?category={category_slug}"
        elif search_query:
            seo_title = f"Search Results for '{search_query}' | FitPulse"
            seo_desc = f"Articles matching your search for '{search_query}' on FitPulse fitness blog."
            canonical = f"{Config.SITE_BASE_URL}/blog"
        else:
            seo_title = "Student Fitness & Nutrition Blog Archive | FitPulse"
            seo_desc = "Browse all evidence-based guides on healthy diet for college students, dorm room workouts, brain foods, and exam recovery routines."
            canonical = f"{Config.SITE_BASE_URL}/blog"

        page_seo = {
            'title': seo_title,
            'description': seo_desc,
            'keywords': 'college fitness blog, student diet tips, dorm health articles, student workout routines',
            'canonical': canonical,
            'og_type': 'blog',
            'og_image': 'https://images.unsplash.com/photo-1517838277536-f5f99be501cd?auto=format&fit=crop&w=1200&q=80'
        }

        return render_template('blog_list.html', 
                               posts=posts, 
                               categories=categories, 
                               active_category=active_category, 
                               search_query=search_query,
                               seo=page_seo)

    @app.route('/blog/<slug>')
    def blog_detail(slug):
        post = Post.query.filter_by(slug=slug).first_or_404()
        
        # Related posts from other articles
        related_posts = Post.query.filter(
            Post.id != post.id
        ).order_by(Post.created_at.desc()).limit(3).all()

        # Previous and Next Article for seamless inter-article navigation
        all_posts = Post.query.order_by(Post.created_at.asc()).all()
        current_idx = next((i for i, p in enumerate(all_posts) if p.id == post.id), None)
        prev_post = all_posts[current_idx - 1] if current_idx is not None and current_idx > 0 else None
        next_post = all_posts[current_idx + 1] if current_idx is not None and current_idx < len(all_posts) - 1 else None
        
        # Dedicated On-Page SEO metadata
        page_seo = {
            'title': post.meta_title,
            'description': post.meta_description,
            'keywords': post.keywords,
            'canonical': f"{Config.SITE_BASE_URL}/blog/{post.slug}",
            'og_type': 'article',
            'og_image': post.featured_image,
            'published_time': post.created_at.isoformat(),
            'modified_time': post.updated_at.isoformat(),
            'author': post.author_name
        }

        return render_template('blog_detail.html', 
                               post=post, 
                               related_posts=related_posts, 
                               prev_post=prev_post,
                               next_post=next_post,
                               seo=page_seo)

    @app.route('/about')
    def about():
        page_seo = {
            'title': 'About FitPulse | College Health, Nutrition & Fitness Project',
            'description': 'FitPulse was founded to make healthy living, budget nutrition, and bodyweight fitness accessible, realistic, and fun for university students worldwide.',
            'keywords': 'about fitpulse, college health team, student fitness mission, health digital marketing',
            'canonical': f"{Config.SITE_BASE_URL}/about",
            'og_type': 'website',
            'og_image': 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1200&q=80'
        }
        return render_template('about.html', seo=page_seo)

    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        if request.method == 'POST':
            name = request.form.get('name', '').strip()
            email = request.form.get('email', '').strip()
            subject = request.form.get('subject', '').strip()
            message = request.form.get('message', '').strip()

            if not name or not email or not message:
                flash('Please complete all required fields.', 'error')
            else:
                try:
                    new_msg = ContactMessage(name=name, email=email, subject=subject or 'General Inquiry', message=message)
                    db.session.add(new_msg)
                    db.session.commit()
                    flash('Thanks for reaching out! We received your message and will respond shortly.', 'success')
                except Exception as e:
                    db.session.rollback()
                    flash('Message received! (Demo mode saved)', 'success')
                return redirect(url_for('contact'))

        page_seo = {
            'title': 'Contact FitPulse | Ask Us Fitness & Nutrition Questions',
            'description': 'Have a question about college meal prep, dorm workouts, or our SEO case study? Get in touch with the FitPulse editorial team today.',
            'keywords': 'contact fitpulse, student wellness contact, college fitness help',
            'canonical': f"{Config.SITE_BASE_URL}/contact",
            'og_type': 'website',
            'og_image': 'https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=1200&q=80'
        }
        return render_template('contact.html', seo=page_seo)

    # ==========================================
    # SEARCH ENGINE OPTIMIZATION (SEO) ROUTES
    # ==========================================

    @app.route('/sitemap.xml')
    def sitemap():
        """
        Dynamically generates XML Sitemap for Google Search Console / Bing Webmaster.
        Lists all static routes and all dynamic blog URLs with timestamps & priority.
        """
        posts = Post.query.order_by(Post.updated_at.desc()).all()
        categories = Category.query.all()
        
        static_pages = [
            {'loc': f"{Config.SITE_BASE_URL}/", 'priority': '1.0', 'changefreq': 'daily', 'lastmod': datetime.utcnow().strftime('%Y-%m-%d')},
            {'loc': f"{Config.SITE_BASE_URL}/blog", 'priority': '0.9', 'changefreq': 'daily', 'lastmod': datetime.utcnow().strftime('%Y-%m-%d')},
            {'loc': f"{Config.SITE_BASE_URL}/about", 'priority': '0.7', 'changefreq': 'monthly', 'lastmod': datetime.utcnow().strftime('%Y-%m-%d')},
            {'loc': f"{Config.SITE_BASE_URL}/contact", 'priority': '0.6', 'changefreq': 'monthly', 'lastmod': datetime.utcnow().strftime('%Y-%m-%d')},
        ]
        
        template = render_template('sitemap.xml', 
                                   static_pages=static_pages, 
                                   posts=posts, 
                                   categories=categories,
                                   base_url=Config.SITE_BASE_URL)
        response = make_response(template)
        response.headers['Content-Type'] = 'application/xml; charset=utf-8'
        return response

    @app.route('/robots.txt')
    def robots():
        """
        Generates standard robots.txt directing search engine crawlers to sitemap.xml.
        """
        sitemap_url = f"{Config.SITE_BASE_URL}/sitemap.xml"
        template = render_template('robots.txt', sitemap_url=sitemap_url)
        response = make_response(template)
        response.headers['Content-Type'] = 'text/plain; charset=utf-8'
        return response

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        # Auto-create tables and auto-seed if empty
        db.create_all()
        if not Post.query.first():
            print("[*] First run detected: Seeding database with SEO sample blogs...")
            from seed import seed_database
            seed_database()
    print("=" * 60)
    print("[*] FitPulse Fitness & SEO Blog is running!")
    print("[-] Local URL: http://127.0.0.1:5000")
    print("[-] Sitemap:   http://127.0.0.1:5000/sitemap.xml")
    print("[-] Robots:    http://127.0.0.1:5000/robots.txt")
    print("=" * 60)
    app.run(debug=True, host='127.0.0.1', port=5000)
