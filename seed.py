import sys
import io
from datetime import datetime, timedelta
from app import create_app
from models import db, Category, Post

# Ensure UTF-8 output on Windows consoles
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def seed_database():
    app = create_app()
    with app.app_context():
        print("[*] Initializing and creating database tables...")
        db.create_all()

        # Check if already seeded
        if Post.query.first():
            print("Database already contains articles. Clearing existing data for fresh seed...")
            Post.query.delete()
            Category.query.delete()
            db.session.commit()

        print("[+] Adding Categories...")
        cat_nutrition = Category(
            name="Dorm Nutrition",
            slug="dorm-nutrition",
            description="Affordable, science-backed eating hacks and meal prep strategies for campus living.",
            badge_color="emerald"
        )
        cat_fitness = Category(
            name="Quick Workouts",
            slug="quick-workouts",
            description="Effective, zero-equipment workouts and bodyweight routines designed for small spaces.",
            badge_color="lime"
        )
        cat_habits = Category(
            name="Mind & Energy",
            slug="mind-and-energy",
            description="Brain foods, sustained mental focus, and practical habits to conquer exam stress.",
            badge_color="indigo"
        )
        cat_recovery = Category(
            name="Sleep & Recovery",
            slug="sleep-recovery",
            description="Circadian rhythm hacks, muscle recovery, and restful sleep routines for busy students.",
            badge_color="amber"
        )

        db.session.add_all([cat_nutrition, cat_fitness, cat_habits, cat_recovery])
        db.session.commit()

        print("[+] Adding SEO-Optimized Health & Fitness Blog Posts...")

        # 1. MAIN BLOG: Healthy Diet for College Students
        p1 = Post(
            title="Healthy Diet for College Students: Budget Meal Prep & Dorm Hacks",
            slug="healthy-diet-for-college-students",
            meta_title="Healthy Diet for College Students: Budget Meal Prep & Dorm Hacks",
            meta_description="Learn how to maintain a healthy diet for college students on a budget. Actionable dorm meal prep tips, cheap grocery lists, and quick no-cook recipes.",
            focus_keyword="healthy diet for college students",
            keywords="healthy diet for college students, college meal prep on a budget, cheap healthy food for students, dorm room healthy snacks, student grocery list, healthy eating habits for university students",
            excerpt="Eating healthy in college doesn't require a ₹5,000 monthly grocery budget or a gourmet kitchen. Here is your ultimate, fluff-free guide to clean nutrition, cheap student groceries under ₹500/week, and microwave dorm hacks.",
            featured_image="https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=1200&q=80",
            image_alt="Healthy diet for college students featuring colorful salad bowl, avocados, fresh vegetables and meal prep containers",
            reading_time="7 min read",
            author_name="Maya Lin",
            author_role="Student Wellness Coach & Nutritionist",
            is_featured=True,
            category_id=cat_nutrition.id,
            created_at=datetime.utcnow() - timedelta(days=2),
            content="""
<p class="lead text-lg text-slate-700 leading-relaxed font-normal mb-6">
Maintaining a <strong>healthy diet for college students</strong> is notoriously difficult. Between 8:00 AM lectures, college assignments, exam stress, and a tight hostel allowance, it is tempting to survive on instant noodles and oily canteen food. However, adopting sustainable <em>healthy eating habits for university students</em> does not require thousands of rupees, complex cooking gadgets, or gourmet chef skills.
</p>

<div class="my-6 p-5 bg-emerald-50 border-l-4 border-emerald-500 rounded-r-xl">
    <p class="text-emerald-900 font-medium"><strong>Key Takeaway:</strong> A sustainable, cheap healthy food strategy for students relies on 4 simple building blocks: complex carbohydrates, affordable lean proteins, healthy fats, and bulk fiber. You can prep 80% of your meals on a budget of just <strong>₹500 to ₹700 per week</strong> using basic appliances like an electric kettle or microwave!</p>
</div>

<h2 id="why-students-struggle" class="text-2xl font-bold text-slate-900 mt-8 mb-4">Why Healthy Eating Feels Impossible in College (And How to Fix It)</h2>
<p class="text-slate-700 leading-relaxed mb-4">
Most university canteens and local food joints prioritize low cost and long shelf life over nutritional quality. Deep-fried snacks and sugary energy drinks create rapid blood sugar spikes followed by severe afternoon brain fog and exhaustion.
</p>

<h3 class="text-xl font-semibold text-slate-800 mt-4 mb-2">The Canteen Convenience Trap</h3>
<p class="text-slate-700 leading-relaxed mb-4">
When you are rushing between classes, whatever is fastest wins. Having pre-portioned <em>dorm room healthy snacks</em> ready in your backpack breaks this dependency and saves up to ₹2,000 every month.
</p>

<h3 class="text-xl font-semibold text-slate-800 mt-4 mb-2">Physical Activity and Nutrient Absorption</h3>
<p class="text-slate-700 leading-relaxed mb-4">
Nutrient partitioning improves dramatically when you stay physically active. Complementing your balanced student diet with our quick <a href="/blog/dorm-room-workout-no-equipment" class="text-emerald-600 font-semibold underline hover:text-emerald-800 transition">20-Minute Dorm Room Workout</a> stimulates insulin sensitivity, accelerates muscle tone, and prevents common freshman fatigue.
</p>

<h2 id="student-grocery-list" class="text-2xl font-bold text-slate-900 mt-8 mb-4">The ₹500/Week Student Grocery List (High Protein, Low Budget)</h2>
<p class="text-slate-700 leading-relaxed mb-4">
To execute effective <strong>college meal prep on a budget</strong>, stick to versatile, non-perishable core items. Buy these staples in bulk at local markets or discount supermarkets:
</p>

<h3 class="text-xl font-semibold text-slate-800 mt-4 mb-2">Complex Carbohydrates & Grains</h3>
<ul class="list-disc pl-6 space-y-2 text-slate-700 mb-4">
    <li><strong>Rolled Oats or Daliya (₹60/500g):</strong> The gold standard of slow-burning complex carbs. Rich in beta-glucan soluble fiber that keeps hunger muted through long 3-hour lab sessions.</li>
    <li><strong>Brown Rice Cups / Whole Wheat Rotis (₹40):</strong> Provides steady glycogen replenishment without energy slumps.</li>
</ul>

<h3 class="text-xl font-semibold text-slate-800 mt-4 mb-2">Affordable Lean Proteins</h3>
<ul class="list-disc pl-6 space-y-2 text-slate-700 mb-4">
    <li><strong>Farm Fresh Eggs (₹80/dozen):</strong> Complete amino acid profile with bioavailable choline to enhance memory retention during study sessions.</li>
    <li><strong>Kala Chana, Kabuli Chana & Green Moong (₹50/pack):</strong> High in plant protein and dietary fiber; boil in bulk or sprout for instant nutrition.</li>
    <li><strong>Soya Chunks or Fresh Paneer (₹60):</strong> Pure protein powerhouse (soya chunks offer 52g protein per 100g at under ₹30).</li>
</ul>

<h3 class="text-xl font-semibold text-slate-800 mt-4 mb-2">Essential Micro-Nutrients & Healthy Fats</h3>
<ul class="list-disc pl-6 space-y-2 text-slate-700 mb-6">
    <li><strong>Roasted Peanuts / Peanut Butter (₹75):</strong> Dense monounsaturated fats that sustain cognitive focus.</li>
    <li><strong>Fresh Seasonal Greens & Palak / Bananas (₹60):</strong> Vital electrolytes (potassium, magnesium) for muscle cramp prevention and stress resilience.</li>
    <li><strong>Fresh Curd / Dahi (₹40):</strong> Natural probiotic that soothes digestion and counters campus stress-induced acidity.</li>
</ul>

<h2 id="dorm-room-hacks" class="text-2xl font-bold text-slate-900 mt-8 mb-4">Dorm Room Meal Prep Hacks Without a Full Kitchen</h2>
<p class="text-slate-700 leading-relaxed mb-4">
Not having access to a full stove or kitchen is no roadblock to eating <em>cheap healthy food for students</em>. These 3 simple methods keep your active prep under 20 minutes:
</p>

<h3 class="text-xl font-semibold text-slate-800 mt-4 mb-2">Hack 1: The Mason Jar Overnight Oats Blueprint</h3>
<p class="text-slate-700 leading-relaxed mb-4">
In a reusable jar, combine 1/2 cup rolled oats, 1 tablespoon chia seeds or roasted flaxseeds, 1 tablespoon peanut butter, and 1/2 cup milk or warm water. Shake and leave in your mini-fridge overnight. Breakfast is ready before you wake up.
</p>

<h3 class="text-xl font-semibold text-slate-800 mt-4 mb-2">Hack 2: Microwave Steam & Poach Technique</h3>
<p class="text-slate-700 leading-relaxed mb-4">
Place frozen vegetables or diced sweet potatoes in a microwave-safe bowl with 2 tablespoons of water. Cover with a plate and microwave for 3 minutes for crisp, nutrient-dense steamed greens.
</p>

<h3 class="text-xl font-semibold text-slate-800 mt-4 mb-2">Hack 3: The 3-Minute High-Protein Salad Wrap</h3>
<p class="text-slate-700 leading-relaxed mb-4">
Rinse boiled chickpeas or shredded boiled eggs. Toss with diced cucumber, tomatoes, a squeeze of lemon, salt, and pepper. Roll into a whole-wheat chapati for a balanced, mess-free portable lunch.
</p>

<h2 id="sample-meal-plan" class="text-2xl font-bold text-slate-900 mt-8 mb-4">5-Day Quick Student Meal Blueprint</h2>
<p class="text-slate-700 leading-relaxed mb-4">
Here is a practical Monday-through-Friday meal breakdown designed around a ₹500 weekly student grocery basket:
</p>
<div class="overflow-x-auto my-6">
    <table class="min-w-full text-left border border-slate-200 rounded-lg overflow-hidden">
        <thead class="bg-slate-100 text-slate-800 font-semibold text-sm">
            <tr>
                <th class="p-3 border-b">Day</th>
                <th class="p-3 border-b">Breakfast</th>
                <th class="p-3 border-b">Lunch</th>
                <th class="p-3 border-b">Dinner</th>
            </tr>
        </thead>
        <tbody class="text-slate-700 text-sm divide-y divide-slate-200">
            <tr>
                <td class="p-3 font-medium text-emerald-700">Monday</td>
                <td class="p-3">Peanut butter & banana overnight oats</td>
                <td class="p-3">Sprouted chana & cucumber whole-wheat wrap</td>
                <td class="p-3">Microwave daliya with steamed palak & curd</td>
            </tr>
            <tr>
                <td class="p-3 font-medium text-emerald-700">Tuesday</td>
                <td class="p-3">2 hard-boiled eggs + sliced apple</td>
                <td class="p-3">Paneer & tomato whole-wheat pita</td>
                <td class="p-3">Brown rice cup + sauteed soya chunks in spices</td>
            </tr>
            <tr>
                <td class="p-3 font-medium text-emerald-700">Wednesday</td>
                <td class="p-3">Fresh dahi bowl with crushed peanuts & banana</td>
                <td class="p-3">Leftover soya chunks & brown rice bowl</td>
                <td class="p-3">Boiled yellow moong dal with warm roti</td>
            </tr>
            <tr>
                <td class="p-3 font-medium text-emerald-700">Thursday</td>
                <td class="p-3">Chia seed & cocoa powder oat pudding</td>
                <td class="p-3">Egg salad sandwich with light curd dressing</td>
                <td class="p-3">Hostel noodle upgrade (add boiled egg + spinach)</td>
            </tr>
            <tr>
                <td class="p-3 font-medium text-emerald-700">Friday</td>
                <td class="p-3">Banana & peanut butter smoothie bowl</td>
                <td class="p-3">Kala chana chaat with lemon & tomatoes</td>
                <td class="p-3">Paneer bhurji wrap with raw cucumber sticks</td>
            </tr>
        </tbody>
    </table>
</div>

<h2 id="healthy-snacking" class="text-2xl font-bold text-slate-900 mt-8 mb-4">Healthy Snacking and Energy Between Lectures</h2>
<p class="text-slate-700 leading-relaxed mb-4">
What you consume between meals dictates your afternoon attention span. Optimize your holistic student routine by exploring our connected guides:
</p>
<ul class="list-disc pl-6 space-y-2 text-slate-700 mb-6">
    <li><strong>Conquer Late-Night Hunger:</strong> Swap high-sugar vending machine biscuits for nutrient-rich snacks from our <a href="/blog/late-night-healthy-study-snacks" class="text-emerald-600 font-semibold underline hover:text-emerald-800">Healthy Study Snacks Guide</a>.</li>
    <li><strong>Avoid Afternoon Fatigue:</strong> Replace commercial energy drinks with clean hydration science outlined in our <a href="/blog/hydration-and-energy-guide-students" class="text-emerald-600 font-semibold underline hover:text-emerald-800">Student Hydration & Energy Guide</a>.</li>
    <li><strong>Optimize Nightly Recovery:</strong> Protect your cognitive memory retention with protocols from our <a href="/blog/sleep-optimization-for-college-students" class="text-emerald-600 font-semibold underline hover:text-emerald-800">Sleep Optimization Guide</a>.</li>
</ul>

<h2 id="faq" class="text-2xl font-bold text-slate-900 mt-8 mb-4">Frequently Asked Questions About College Nutrition</h2>
<div class="space-y-4 mb-8">
    <div class="p-4 bg-slate-50 rounded-lg border border-slate-200">
        <h3 class="font-semibold text-slate-900">How much does a healthy diet for college students cost per week?</h3>
        <p class="text-slate-700 text-sm mt-1">With smart bulk purchasing (rolled oats, eggs, daliya, seasonal greens, and chana/sprouts), students can comfortably eat nutritious, wholesome meals for ₹500 to ₹700 per week—far cheaper than eating oily mess food or ordering food delivery every night.</p>
    </div>
    <div class="p-4 bg-slate-50 rounded-lg border border-slate-200">
        <h3 class="font-semibold text-slate-900">Can I build muscle on a budget college diet?</h3>
        <p class="text-slate-700 text-sm mt-1">Yes! Eggs, paneer, soya chunks, Greek-style dahi, and legumes provide complete amino acid profiles required for hypertrophy without requiring expensive imported whey protein.</p>
    </div>
</div>

<h2 id="call-to-action" class="text-2xl font-bold text-slate-900 mt-8 mb-4">Start Your Student Nutrition Transformation Today</h2>
<div class="my-6 p-6 rounded-2xl bg-gradient-to-r from-emerald-600 to-teal-700 text-white shadow-lg space-y-4">
    <h3 class="text-xl font-bold text-white">Take the Next Step in Your College Fitness Journey</h3>
    <p class="text-emerald-100 text-sm leading-relaxed">
        Healthy eating is just one half of the equation. Combine this budget nutrition blueprint with regular bodyweight training to maximize your energy, confidence, and academic grades.
    </p>
    <div class="flex flex-wrap gap-3 pt-2">
        <a href="/blog/dorm-room-workout-no-equipment" class="px-5 py-2.5 rounded-xl bg-white text-emerald-800 text-xs font-bold hover:bg-emerald-50 transition shadow-sm inline-flex items-center gap-1.5">
            <span>Explore 20-Minute Dorm Workout</span>
            <span>&rarr;</span>
        </a>
        <a href="/contact" class="px-5 py-2.5 rounded-xl bg-emerald-800 text-white text-xs font-bold hover:bg-emerald-900 transition border border-emerald-500/50">
            Ask a Nutrition Question
        </a>
    </div>
</div>
"""
        )

        # 2. BLOG: 20-Minute Dorm Room Workout
        p2 = Post(
            title="The 20-Minute Dorm Room Workout: Build Muscle Without Equipment",
            slug="dorm-room-workout-no-equipment",
            meta_title="20-Minute Dorm Room Workout: Full Body Routine (No Equipment)",
            meta_description="Short on gym time? Build muscle and stay fit with this 20-minute dorm room workout designed specifically for busy college students without equipment.",
            focus_keyword="dorm room workout",
            keywords="dorm room workout, bodyweight exercise for students, college fitness routine, home workout no equipment, student calisthenics",
            excerpt="No gym membership? Tiny 10x10 dorm space? No problem. Try this high-efficiency 20-minute bodyweight routine to torch fat, increase energy, and build athletic muscle.",
            featured_image="https://images.unsplash.com/photo-1517838277536-f5f99be501cd?auto=format&fit=crop&w=1200&q=80",
            image_alt="Student performing pushups on floor in college dorm room for bodyweight workout",
            reading_time="5 min read",
            author_name="Jordan Reed",
            author_role="CSCS Strength & Conditioning Coach",
            is_featured=True,
            category_id=cat_fitness.id,
            created_at=datetime.utcnow() - timedelta(days=4),
            content="""
<p class="lead text-lg text-slate-700 leading-relaxed font-normal mb-6">
Between back-to-back lectures and late-night study sessions, walking 25 minutes across campus to wait in line for a gym bench is the last thing you want to do. The solution? A dedicated <strong>dorm room workout</strong> that activates every major muscle group in only 20 minutes without a single dumbbell.
</p>

<h2 class="text-2xl font-bold text-slate-900 mt-8 mb-4">Why Bodyweight Calisthenics Work for College Students</h2>
<p class="text-slate-700 leading-relaxed mb-4">
Calisthenics utilize progressive angles, mechanical leverage, and high time-under-tension. Science confirms that performing compound bodyweight movements to near-failure produces comparable hypertrophy to free weights—while protecting student joints and taking up zero square footage.
</p>

<h2 class="text-2xl font-bold text-slate-900 mt-8 mb-4">The 4-Movement Dorm Room Circuit</h2>
<p class="text-slate-700 leading-relaxed mb-4">Perform each movement for 45 seconds, followed by 15 seconds of rest. Complete 4 full rounds (total: 20 minutes):</p>
<ul class="list-disc pl-6 space-y-3 text-slate-700 mb-6">
    <li><strong>1. Tempo Desk / Floor Push-Ups:</strong> 3 seconds down, explosive press up. Engages chest, triceps, and anterior deltoids. If floor pushups are tough, incline your hands against your sturdy dorm desk.</li>
    <li><strong>2. Paused Chair Squats & Bulgarian Split Squats:</strong> Place your rear foot on your desk chair and squat deeply on the front leg. Unlocks brutal quad and glute strength.</li>
    <li><strong>3. Doorframe Body Rows / Isometric Towel Pulls:</strong> Wrap a towel around a secure door handle or grip a solid doorway molding to activate your lats, rhomboids, and biceps.</li>
    <li><strong>4. Hollow Body Rockers & Plank Taps:</strong> The ultimate core stabilizer that counteracts hours of hunching over a laptop in the library.</li>
</ul>

<div class="my-6 p-5 bg-lime-50 border-l-4 border-lime-500 rounded-r-xl">
    <p class="text-lime-900"><strong>Recovery Tip:</strong> Muscle growth happens when you sleep and refuel. Fuel your training with our <a href="/blog/healthy-diet-for-college-students" class="text-lime-800 font-bold underline">Healthy Diet for College Students</a> meal plan and optimize your sleep schedule with our <a href="/blog/sleep-optimization-for-college-students" class="text-lime-800 font-bold underline">Sleep Optimization Guide</a>.</p>
</div>
"""
        )

        # 3. BLOG: Mindful Snacking & Late-Night Study Cravings
        p3 = Post(
            title="Mindful Snacking: How to Beat Late-Night Study Cravings",
            slug="late-night-healthy-study-snacks",
            meta_title="Healthy Study Snacks for College Students: Stop Late Cravings",
            meta_description="Avoid sugar crashes during finals! Discover 9 healthy study snacks for college students that boost focus, memory, and sustained energy without empty calories.",
            focus_keyword="healthy study snacks",
            keywords="healthy study snacks, late night snacks for college, brain foods for studying, student exam snacks, sugar crash prevention",
            excerpt="Don't let 1:00 AM vending machine binges derail your exam focus. Discover smart, brain-boosting study snacks that nourish cognitive retention and crush midnight hunger.",
            featured_image="https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=1200&q=80",
            image_alt="Healthy study snacks including nuts, dark chocolate, fresh berries and sliced apples on student desk with notebook",
            reading_time="4 min read",
            author_name="Maya Lin",
            author_role="Student Wellness Coach & Nutritionist",
            is_featured=False,
            category_id=cat_habits.id,
            created_at=datetime.utcnow() - timedelta(days=6),
            content="""
<p class="lead text-lg text-slate-700 leading-relaxed font-normal mb-6">
When midterms roll around, 11:00 PM cravings strike hard. The immediate reaction is to grab high-sodium chips or sugary cookies. But the subsequent insulin spike causes extreme brain fog within 45 minutes. Choosing nutrient-dense <strong>healthy study snacks</strong> stabilizes your neurotransmitters so you can retain critical formulas and concepts.
</p>

<h2 class="text-2xl font-bold text-slate-900 mt-8 mb-4">The Top 5 Brain-Power Snacks for Exam Week</h2>
<ol class="list-decimal pl-6 space-y-3 text-slate-700 mb-6">
    <li><strong>Dark Chocolate (70%+) & Raw Walnuts:</strong> Walnuts are rich in DHA (an omega-3 fatty acid) while dark chocolate provides flavonoids that enhance cerebral blood flow.</li>
    <li><strong>Apple Slices with Natural Peanut Butter:</strong> The pectin fiber in apples slows sugar absorption, while healthy fats keep hunger hormones (ghrelin) silenced.</li>
    <li><strong>Air-Popped Stovetop / Microwave Popcorn:</strong> A whole grain packed with volume and polyphenols. Season with nutritional yeast for a cheesy, vitamin B12-rich kick.</li>
    <li><strong>Roasted Edamame:</strong> 14 grams of plant protein per cup with crunch that rivals potato chips.</li>
    <li><strong>Greek Yogurt with Cinnamon:</strong> Casein protein digests slowly throughout the night, preventing midnight stomach rumbles without disrupting sleep.</li>
</ol>

<p class="text-slate-700 leading-relaxed mb-4">
Combine these snacks with good hydration—read our <a href="/blog/hydration-and-energy-guide-students" class="text-indigo-600 font-semibold underline">Student Hydration & Energy Guide</a> to learn why dehydration is frequently misread by your brain as food cravings!
</p>
"""
        )

        # 4. BLOG: Hydration & Energy During Exam Week
        p4 = Post(
            title="Hydration & Energy: Ditch the Sugar Crashes During Exam Week",
            slug="hydration-and-energy-guide-students",
            meta_title="Student Hydration & Energy Guide: Stop Sugar Crashes in Exams",
            meta_description="Tired of relying on energy drinks during exam season? Learn how proper hydration and smart nutrition give college students clean, all-day mental focus.",
            focus_keyword="energy hacks for college students",
            keywords="energy hacks for college students, student hydration, exam focus, clean caffeine alternatives, natural student energy, electrolytes dorm",
            excerpt="Are 300mg caffeine energy drinks leaving you jittery and crashing mid-exam? Discover how cellular hydration and electrolyte balance sustain sharp memory recall.",
            featured_image="https://images.unsplash.com/photo-1559839914-ba2ce56d21f7?auto=format&fit=crop&w=1200&q=80",
            image_alt="Student drinking clean water from reusable bottle next to study textbooks in campus library",
            reading_time="5 min read",
            author_name="Jordan Reed",
            author_role="CSCS Strength & Conditioning Coach",
            is_featured=False,
            category_id=cat_habits.id,
            created_at=datetime.utcnow() - timedelta(days=8),
            content="""
<p class="lead text-lg text-slate-700 leading-relaxed font-normal mb-6">
During exam preparation, college students drink commercial energy drinks at alarming rates. While caffeine momentarily blocks adenosine receptors, it does nothing to restore cellular ATP. For true, sustained stamina, modern students need smarter <strong>energy hacks for college students</strong> centered on hydration science.
</p>

<h2 class="text-2xl font-bold text-slate-900 mt-8 mb-4">The Cost of Mild Dehydration on Academic Performance</h2>
<p class="text-slate-700 leading-relaxed mb-4">
Clinical studies from the Journal of Nutrition demonstrate that even a 1.5% decrease in body water percentage impairs working memory, heightens anxiety, and causes headaches. Often when you feel exhausted in class, your brain is simply starved for water and electrolytes.
</p>

<h2 class="text-2xl font-bold text-slate-900 mt-8 mb-4">The Homemade Student Electrolyte Tonic</h2>
<p class="text-slate-700 leading-relaxed mb-4">Skip ₹120 commercial sports drinks loaded with artificial dyes and refined sugars. Mix this quick student hydration tonic in your reusable bottle:</p>
<ul class="list-disc pl-6 space-y-2 text-slate-700 mb-6">
    <li>750ml filtered water</li>
    <li>Juice of 1/2 fresh lemon (potassium & vitamin C)</li>
    <li>1 pinch of pink Himalayan or rock salt / sendha namak (essential sodium)</li>
    <li>1 teaspoon raw honey or jaggery (trace glucose for fast cellular uptake)</li>
</ul>

<p class="text-slate-700 leading-relaxed mb-4">
Combine this tonic with our full <a href="/blog/healthy-diet-for-college-students" class="text-indigo-600 font-semibold underline">Healthy Diet for College Students</a> guide to permanently banish afternoon fatigue.
</p>
"""
        )

        # 5. BLOG: Sleep Optimization for College Students
        p5 = Post(
            title="Sleep Optimization for College Students: Hack Your Recovery & Grades",
            slug="sleep-optimization-for-college-students",
            meta_title="Sleep Optimization for College Students: Better Grades & Rest",
            meta_description="Struggling with insomnia and all-nighters? Discover practical sleep optimization routines that improve student cognitive retention, muscle recovery, and mood.",
            focus_keyword="sleep optimization for students",
            keywords="sleep optimization for students, college sleep schedule, circadian rhythm dorm, fix sleep schedule finals, academic memory consolidation",
            excerpt="All-nighters do not work. Science proves that memory consolidation and muscle repair happen strictly in deep NREM and REM cycles. Here is your dorm sleep playbook.",
            featured_image="https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?auto=format&fit=crop&w=1200&q=80",
            image_alt="Peaceful student bedroom with soft morning light showing clean bed and relaxed atmosphere for sleep recovery",
            reading_time="6 min read",
            author_name="Dr. Elena Vance",
            author_role="Circadian Biology & Sleep Researcher",
            is_featured=True,
            category_id=cat_recovery.id,
            created_at=datetime.utcnow() - timedelta(days=10),
            content="""
<p class="lead text-lg text-slate-700 leading-relaxed font-normal mb-6">
The college myth that "sleep is for the weak" has been completely dismantled by neuroscience. Pulling an all-nighter reduces your cognitive processing speed by 40%—the neurological equivalent of being legally intoxicated. Mastering <strong>sleep optimization for students</strong> is the single highest-ROI habit for both GPA and physical fitness.
</p>

<h2 class="text-2xl font-bold text-slate-900 mt-8 mb-4">How Sleep Consolidates Academic Memory</h2>
<p class="text-slate-700 leading-relaxed mb-4">
During Slow-Wave Sleep (deep sleep), your brain's hippocampus transfers newly acquired facts and concepts into the permanent neocortex. Without this sleep phase, up to 70% of what you reviewed during the day is lost by morning.
</p>

<h2 class="text-2xl font-bold text-slate-900 mt-8 mb-4">The 4-Step Dorm Room Sleep Protocol</h2>
<ol class="list-decimal pl-6 space-y-3 text-slate-700 mb-6">
    <li><strong>Get Sunlight within 30 Minutes of Waking:</strong> Stepping outside for 10 minutes sets your circadian timer, ensuring melatonin release begins 14 hours later.</li>
    <li><strong>Implement the 10-3-2-1 Rule:</strong>
        <ul class="list-disc pl-6 mt-2 space-y-1">
            <li>10 hours before bed: No more caffeine.</li>
            <li>3 hours before bed: No heavy meals (stick to light <a href="/blog/late-night-healthy-study-snacks" class="text-amber-700 font-semibold underline">Healthy Study Snacks</a>).</li>
            <li>2 hours before bed: Stop studying or doing intense mental tasks.</li>
            <li>1 hour before bed: Turn off harsh blue-light screens or wear blue-blocking glasses.</li>
        </ul>
    </li>
    <li><strong>Create Pitch Darkness in Shared Rooms:</strong> Invest ₹200 to ₹300 in a contoured 3D eye mask and soft earplugs to block hostel corridor light and roommate study lamps.</li>
    <li><strong>Cool Down Your Sleep Environment:</strong> Your body must drop by 1 to 2 degrees Celsius to trigger deep sleep. Keep your window cracked or use a clip-on fan.</li>
</ol>

<p class="text-slate-700 leading-relaxed mb-4">
Physical training also speeds up sleep onset latency. Combine this sleep routine with our <a href="/blog/dorm-room-workout-no-equipment" class="text-amber-700 font-semibold underline">20-Minute Dorm Room Workout</a> and <a href="/blog/healthy-diet-for-college-students" class="text-amber-700 font-semibold underline">Healthy Diet for College Students</a> for peak academic and physical conditioning!
</p>
"""
        )

        db.session.add_all([p1, p2, p3, p4, p5])
        db.session.commit()
        print("[SUCCESS] Database successfully seeded with 4 categories and 5 high-converting SEO articles!")

if __name__ == '__main__':
    seed_database()
