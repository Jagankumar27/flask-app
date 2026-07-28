from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>CarePlus Multi Speciality Hospital</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:'Poppins',sans-serif;
scroll-behavior:smooth;
}

body{

background:#f5fbff;
color:#333;
overflow-x:hidden;

}

/* Loader */

.loader{

position:fixed;
top:0;
left:0;
width:100%;
height:100vh;
background:white;

display:flex;
justify-content:center;
align-items:center;

z-index:99999;

animation:loaderHide 2s forwards;
animation-delay:2s;

}

.loader span{

width:70px;
height:70px;

border:8px solid #caf0f8;
border-top:8px solid #0077b6;

border-radius:50%;

animation:spin 1s linear infinite;

}

@keyframes spin{

100%{

transform:rotate(360deg);

}

}

@keyframes loaderHide{

100%{

opacity:0;
visibility:hidden;

}

}

/* Top Bar */

.top-bar{

background:#003566;
color:white;

padding:10px;

text-align:center;

font-size:15px;

}

/* Header */

header{

position:sticky;

top:0;

display:flex;

justify-content:space-between;

align-items:center;

padding:18px 60px;

background:linear-gradient(90deg,#0056b3,#0096c7,#00c2a8);

box-shadow:0 5px 20px rgba(0,0,0,.15);

z-index:1000;

}

.logo{

font-size:34px;
font-weight:700;
color:white;

}

nav a{

color:white;

text-decoration:none;

margin-left:25px;

font-size:18px;

transition:.4s;

}

nav a:hover{

color:#ffe66d;

}

/* Dark Mode Button */

.mode{

background:white;

color:#0077b6;

padding:10px 18px;

border-radius:30px;

font-weight:bold;

cursor:pointer;

}

/* Hero */

.hero{

height:90vh;

background:
linear-gradient(rgba(0,0,0,.55),
rgba(0,0,0,.55)),

url("https://images.unsplash.com/photo-1586773860418-d37222d8fce3?auto=format&fit=crop&w=1600&q=80");

background-size:cover;
background-position:center;

display:flex;
justify-content:center;
align-items:center;
flex-direction:column;

text-align:center;

color:white;

padding:20px;

}

.hero h1{

font-size:68px;

font-weight:700;

animation:fadeDown 1s;

}

.hero p{

font-size:24px;

margin-top:20px;

animation:fadeUp 2s;

}

.hero button{

margin-top:35px;

padding:18px 45px;

border:none;

background:#00c896;

color:white;

font-size:20px;

border-radius:50px;

cursor:pointer;

transition:.4s;

animation:fadeUp 3s;

}

.hero button:hover{

background:#009966;

transform:translateY(-5px);

}

@keyframes fadeDown{

from{

opacity:0;
transform:translateY(-50px);

}

to{

opacity:1;
transform:translateY(0);

}

}

@keyframes fadeUp{

from{

opacity:0;
transform:translateY(60px);

}

to{

opacity:1;
transform:translateY(0);

}

}

/* Emergency */

.emergency{

background:#d90429;

color:white;

padding:18px;

text-align:center;

font-size:22px;

font-weight:bold;

animation:blink 1s infinite;

}

@keyframes blink{

50%{

opacity:.6;

}

}

/* Common */

.section-title{

text-align:center;

font-size:45px;

color:#023e8a;

margin:70px 0 40px;

}

.grid{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(260px,1fr));

gap:30px;

padding:20px 60px 60px;

}

.card{

background:white;

padding:30px;

border-radius:20px;

text-align:center;

box-shadow:0 10px 20px rgba(0,0,0,.12);

transition:.4s;

}

.card:hover{

transform:translateY(-12px);

box-shadow:0 15px 30px rgba(0,119,182,.25);

}

.card .icon{

font-size:60px;

}

.card h3{

margin:15px 0;

color:#0077b6;

}

/* Responsive */

@media(max-width:768px){

header{

flex-direction:column;

padding:20px;

}

nav{

margin-top:20px;

}

nav a{

display:block;

margin:10px;

}

.hero h1{

font-size:42px;

}

.hero p{

font-size:18px;

}

}

</style>

</head>

<body>

<div class="loader">

<span></span>

</div>

<div class="top-bar">

🏥 NABH Accredited Hospital |
🚑 24×7 Emergency |
📞 +91 9876543210 |
✉ careplus@hospital.com

</div>

<header>

<div class="logo">

🏥 CarePlus Hospital

</div>

<nav>

<a href="#">Home</a>

<a href="#services">Services</a>

<a href="#departments">Departments</a>

<a href="#doctors">Doctors</a>

<a href="#appointment">Appointment</a>

<a href="#contact">Contact</a>

</nav>

<div class="mode">

🌙 Dark

</div>

</header>

<div class="emergency">

🚑 Emergency Helpline : +91 9876543210

</div>

<section class="hero">

<h1>Advanced Healthcare For Everyone</h1>

<p>

Expert Doctors • Modern Technology • 24×7 Emergency Care

</p>

<button>

Book Appointment

</button>

</section><!-- ================= SERVICES ================= -->

<h2 class="section-title" id="services">Our Medical Services</h2>

<section class="grid">

    <div class="card">
        <div class="icon">🚑</div>
        <h3>Emergency Care</h3>
        <p>
            24×7 emergency services with advanced ambulances,
            trauma specialists, and ICU support.
        </p>
    </div>

    <div class="card">
        <div class="icon">❤️</div>
        <h3>Cardiology</h3>
        <p>
            Complete heart care including ECG, Echo,
            Angiography, and Cardiac Surgery.
        </p>
    </div>

    <div class="card">
        <div class="icon">🧠</div>
        <h3>Neurology</h3>
        <p>
            Specialized treatment for brain,
            spinal cord, and nervous system disorders.
        </p>
    </div>

    <div class="card">
        <div class="icon">🦴</div>
        <h3>Orthopedics</h3>
        <p>
            Joint replacement, fracture care,
            sports injuries, and physiotherapy.
        </p>
    </div>

    <div class="card">
        <div class="icon">🧪</div>
        <h3>Laboratory</h3>
        <p>
            Fully automated pathology lab with
            accurate and fast reports.
        </p>
    </div>

    <div class="card">
        <div class="icon">💊</div>
        <h3>Pharmacy</h3>
        <p>
            24-hour pharmacy providing genuine medicines
            and healthcare products.
        </p>
    </div>

    <div class="card">
        <div class="icon">👶</div>
        <h3>Pediatrics</h3>
        <p>
            Comprehensive healthcare for newborns,
            infants, children, and teenagers.
        </p>
    </div>

    <div class="card">
        <div class="icon">👁️</div>
        <h3>Eye Care</h3>
        <p>
            Cataract surgery, retina treatment,
            glaucoma care, and LASIK services.
        </p>
    </div>

</section>

<!-- ================= DEPARTMENTS ================= -->

<h2 class="section-title" id="departments">
Hospital Departments
</h2>

<section class="grid">

    <div class="card">
        <div class="icon">🏥</div>
        <h3>General Medicine</h3>
        <p>
            Complete diagnosis and treatment
            for common illnesses.
        </p>
    </div>

    <div class="card">
        <div class="icon">❤️</div>
        <h3>Heart Institute</h3>
        <p>
            Advanced cardiac care with experienced
            heart specialists.
        </p>
    </div>

    <div class="card">
        <div class="icon">🫁</div>
        <h3>Pulmonology</h3>
        <p>
            Lung disease treatment,
            asthma care, and respiratory support.
        </p>
    </div>

    <div class="card">
        <div class="icon">🦷</div>
        <h3>Dental Care</h3>
        <p>
            Cosmetic dentistry,
            implants, braces,
            and oral surgery.
        </p>
    </div>

    <div class="card">
        <div class="icon">🤰</div>
        <h3>Gynecology</h3>
        <p>
            Women's healthcare,
            pregnancy care,
            and fertility treatments.
        </p>
    </div>

    <div class="card">
        <div class="icon">🧬</div>
        <h3>Oncology</h3>
        <p>
            Comprehensive cancer diagnosis,
            chemotherapy,
            and radiation therapy.
        </p>
    </div>

    <div class="card">
        <div class="icon">🩹</div>
        <h3>General Surgery</h3>
        <p>
            Minimally invasive and advanced
            surgical procedures.
        </p>
    </div>

    <div class="card">
        <div class="icon">🩺</div>
        <h3>Health Checkup</h3>
        <p>
            Preventive health screening
            packages for every age group.
        </p>
    </div>

</section>

<!-- ================= WHY CHOOSE US ================= -->

<h2 class="section-title">
Why Choose CarePlus?
</h2>

<section class="grid">

    <div class="card">
        <div class="icon">⭐</div>
        <h3>25+ Years Experience</h3>
        <p>
            Trusted healthcare provider with thousands
            of successful treatments.
        </p>
    </div>

    <div class="card">
        <div class="icon">👨‍⚕️</div>
        <h3>120+ Specialists</h3>
        <p>
            Highly qualified doctors
            across multiple specialties.
        </p>
    </div>

    <div class="card">
        <div class="icon">🏆</div>
        <h3>NABH Certified</h3>
        <p>
            International standards of
            patient safety and quality care.
        </p>
    </div>

    <div class="card">
        <div class="icon">⏰</div>
        <h3>24×7 Support</h3>
        <p>
            Emergency doctors,
            ICU,
            pharmacy,
            and ambulance services.
        </p>
    </div>

</section>

<!-- ================= HEALTH PACKAGES ================= -->

<h2 class="section-title">
Health Packages
</h2>

<section class="grid">

    <div class="card">
        <div class="icon">🥉</div>
        <h3>Basic Checkup</h3>
        <h2 style="color:#0077b6;">$19</h2>
        <p>Blood Test</p>
        <p>ECG</p>
        <p>Blood Sugar</p>
        <p>Doctor Consultation</p>
    </div>

    <div class="card">
        <div class="icon">🥈</div>
        <h3>Family Package</h3>
        <h2 style="color:#00a86b;">$49</h2>
        <p>Full Body Checkup</p>
        <p>X-Ray</p>
        <p>ECG</p>
        <p>Vitamin Test</p>
        <p>Doctor Consultation</p>
    </div>

    <div class="card">
        <div class="icon">🥇</div>
        <h3>Premium Package</h3>
        <h2 style="color:#ff6600;">$99</h2>
        <p>MRI Scan</p>
        <p>CT Scan</p>
        <p>Heart Checkup</p>
        <p>Complete Blood Test</p>
        <p>Specialist Consultation</p>
    </div>

</section>
<!-- ================= DOCTORS ================= -->

<h2 class="section-title" id="doctors">
Meet Our Specialists
</h2>

<section class="grid">

<div class="doctor">

<img src="https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?auto=format&fit=crop&w=900&q=80">

<div style="padding:20px;">

<h3>Dr. John Smith</h3>

<p><b>Senior Cardiologist</b></p>

<p>⭐ ⭐ ⭐ ⭐ ⭐</p>

<p>15+ Years Experience</p>

<p>1200+ Successful Surgeries</p>

</div>

</div>

<div class="doctor">

<img src="https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=900&q=80">

<div style="padding:20px;">

<h3>Dr. Sarah Johnson</h3>

<p><b>Neurologist</b></p>

<p>⭐ ⭐ ⭐ ⭐ ⭐</p>

<p>12+ Years Experience</p>

<p>900+ Happy Patients</p>

</div>

</div>

<div class="doctor">

<img src="https://images.unsplash.com/photo-1594824476967-48c8b964273f?auto=format&fit=crop&w=900&q=80">

<div style="padding:20px;">

<h3>Dr. David Lee</h3>

<p><b>Orthopedic Surgeon</b></p>

<p>⭐ ⭐ ⭐ ⭐ ⭐</p>

<p>18+ Years Experience</p>

<p>1500+ Knee Replacements</p>

</div>

</div>

<div class="doctor">

<img src="https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&w=900&q=80">

<div style="padding:20px;">

<h3>Dr. Emily Brown</h3>

<p><b>Pediatrician</b></p>

<p>⭐ ⭐ ⭐ ⭐ ⭐</p>

<p>10+ Years Experience</p>

<p>3000+ Child Consultations</p>

</div>

</div>

</section>

<!-- ================= HOSPITAL STATISTICS ================= -->

<section class="stats">

<div>

<h2 id="patients">
15000+
</h2>

<p>Happy Patients</p>

</div>

<div>

<h2 id="doctors">
120+
</h2>

<p>Expert Doctors</p>

</div>

<div>

<h2 id="departments">
40+
</h2>

<p>Departments</p>

</div>

<div>

<h2 id="awards">
35+
</h2>

<p>Awards</p>

</div>

<div>

<h2 id="operations">
9000+
</h2>

<p>Successful Surgeries</p>

</div>

</section>

<!-- ================= WHY PATIENTS LOVE US ================= -->

<h2 class="section-title">

Why Patients Love Us

</h2>

<section class="grid">

<div class="card">

<div class="icon">
🏥
</div>

<h3>World Class Infrastructure</h3>

<p>

Modern operation theatres, ICU,
MRI, CT Scan,
Digital Laboratory,
Private Rooms and Smart Wards.

</p>

</div>

<div class="card">

<div class="icon">
👨‍⚕️
</div>

<h3>Experienced Doctors</h3>

<p>

Specialists from India's top
medical institutions delivering
quality healthcare.

</p>

</div>

<div class="card">

<div class="icon">
💙
</div>

<h3>Patient First</h3>

<p>

Every patient receives
personalized treatment plans
and compassionate care.

</p>

</div>

<div class="card">

<div class="icon">
🚑
</div>

<h3>Fast Emergency</h3>

<p>

Emergency ambulance reaches
within minutes with trained
medical staff.

</p>

</div>

</section>

<!-- ================= LATEST NEWS ================= -->

<h2 class="section-title">

Latest News

</h2>

<section class="grid">

<div class="card">

<div class="icon">
🩸
</div>

<h3>Blood Donation Camp</h3>

<p>

Join our free blood donation
camp on Sunday from
9 AM to 4 PM.

</p>

</div>

<div class="card">

<div class="icon">
❤️
</div>

<h3>Free Heart Checkup</h3>

<p>

Free ECG and Blood Pressure
screening for senior citizens.

</p>

</div>

<div class="card">

<div class="icon">
💉
</div>

<h3>Vaccination Drive</h3>

<p>

Vaccines available for
children and adults every day.

</p>

</div>

<div class="card">

<div class="icon">
🏥
</div>

<h3>New MRI Machine</h3>

<p>

State-of-the-art MRI
scanner installed with
high precision imaging.

</p>

</div>

</section>

<!-- ================= HOSPITAL GALLERY ================= -->

<h2 class="section-title">Hospital Gallery</h2>

<section class="grid">

<div class="doctor">
<img src="https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?auto=format&fit=crop&w=900&q=80">
</div>

<div class="doctor">
<img src="https://images.unsplash.com/photo-1538108149393-fbbd81895907?auto=format&fit=crop&w=900&q=80">
</div>

<div class="doctor">
<img src="https://images.unsplash.com/photo-1576091160550-2173dba999ef?auto=format&fit=crop&w=900&q=80">
</div>

<div class="doctor">
<img src="https://images.unsplash.com/photo-1580281657527-47f249e8f4df?auto=format&fit=crop&w=900&q=80">
</div>

</section>

<!-- ================= APPOINTMENT ================= -->

<section class="appointment" id="appointment">

<h2 class="section-title">Book Your Appointment</h2>

<form onsubmit="bookAppointment(event)">

<input type="text" placeholder="Full Name" required>

<input type="email" placeholder="Email Address" required>

<input type="tel" placeholder="Phone Number" required>

<input type="date" required>

<input type="time" required>

<select required>

<option value="">Select Department</option>

<option>Cardiology</option>

<option>Neurology</option>

<option>Orthopedics</option>

<option>Pediatrics</option>

<option>Dental</option>

<option>General Medicine</option>

</select>

<textarea rows="5" placeholder="Describe your health problem"></textarea>

<input type="submit" value="Book Appointment">

</form>

</section>

<!-- ================= TESTIMONIALS ================= -->

<h2 class="section-title">Patient Testimonials</h2>

<section style="padding:40px;">

<div class="card" style="max-width:800px;margin:auto;">

<h3 id="patientName">Rahul Sharma</h3>

<p id="patientReview">

Excellent doctors and friendly staff. My surgery was successful and I recovered quickly.

</p>

</div>

</section>

<!-- ================= FAQ ================= -->

<h2 class="section-title">Frequently Asked Questions</h2>

<section style="max-width:900px;margin:auto;padding:30px;">

<details class="card">

<summary><b>Do you provide emergency services?</b></summary>

<p style="margin-top:15px;">
Yes. Emergency care is available 24 hours every day.
</p>

</details>

<br>

<details class="card">

<summary><b>Can I book appointments online?</b></summary>

<p style="margin-top:15px;">
Yes. You can easily book appointments through this website.
</p>

</details>

<br>

<details class="card">

<summary><b>Do you accept insurance?</b></summary>

<p style="margin-top:15px;">
Yes. Most major insurance providers are accepted.
</p>

</details>

<br>

<details class="card">

<summary><b>Is pharmacy available 24×7?</b></summary>

<p style="margin-top:15px;">
Yes. Our pharmacy remains open all day and night.
</p>

</details>

</section>

<!-- ================= CONTACT ================= -->

<section id="contact">

<h2 class="section-title">Contact Us</h2>

<div class="grid">

<div class="card">

<h3>📍 Address</h3>

<p>

CarePlus Multi Speciality Hospital<br>

Hyderabad, Telangana

</p>

</div>

<div class="card">

<h3>☎ Phone</h3>

<p>

+91 9876543210

</p>

</div>

<div class="card">

<h3>✉ Email</h3>

<p>

careplus@hospital.com

</p>

</div>

<div class="card">

<h3>🕒 Working Hours</h3>

<p>

Monday - Sunday

<br>

Open 24 Hours

</p>

</div>

</div>

</section>

<!-- ================= GOOGLE MAP ================= -->

<h2 class="section-title">Find Us</h2>

<div style="padding:40px;">

<iframe

src="https://maps.google.com/maps?q=Hyderabad&t=&z=13&ie=UTF8&iwloc=&output=embed"

width="100%"

height="450"

style="border:0;border-radius:20px;"

loading="lazy">

</iframe>

</div>

<!-- ================= FLOATING BUTTONS ================= -->

<a href="https://wa.me/919876543210"
class="whatsapp"
target="_blank">

💬

</a>

<button id="topBtn"
onclick="topFunction()">

⬆

</button>

<!-- ================= FOOTER ================= -->

<footer>

<h2>🏥 CarePlus Multi Speciality Hospital</h2>

<br>

<p>

Providing quality healthcare with experienced doctors,
advanced medical equipment and compassionate care.

</p>

<br>

<p>

📍 Hyderabad, Telangana

</p>

<p>

☎ +91 9876543210

</p>

<p>

✉ careplus@hospital.com

</p>

<br>

<div style="font-size:32px;">

🌐 📘 📸 ▶️ 💼

</div>

<br>

<p>

© 2026 CarePlus Hospital.
All Rights Reserved.

</p>

</footer>

<style>

footer{

background:#023e8a;

color:white;

text-align:center;

padding:60px 20px;

margin-top:60px;

}

.whatsapp{

position:fixed;

bottom:90px;

right:25px;

width:65px;

height:65px;

border-radius:50%;

background:#25D366;

display:flex;

justify-content:center;

align-items:center;

font-size:34px;

text-decoration:none;

box-shadow:0 10px 20px rgba(0,0,0,.3);

transition:.3s;

z-index:1000;

}

.whatsapp:hover{

transform:scale(1.1);

}

#topBtn{

position:fixed;

bottom:20px;

right:25px;

width:60px;

height:60px;

border:none;

border-radius:50%;

background:#0077b6;

color:white;

font-size:22px;

cursor:pointer;

display:none;

box-shadow:0 8px 18px rgba(0,0,0,.3);

}

.dark{

background:#121212;

color:white;

}

.dark .card{

background:#1e1e1e;

color:white;

}

.dark footer{

background:black;

}

.dark .appointment{

background:#1b263b;

}

.dark input,

.dark textarea,

.dark select{

background:#2b2b2b;

color:white;

border:1px solid #555;

}

</style>

<script>

/* Appointment */

function bookAppointment(e){

e.preventDefault();

alert("✅ Appointment Booked Successfully!");

}

/* Scroll Button */

let topBtn=document.getElementById("topBtn");

window.onscroll=function(){

if(document.body.scrollTop>300 ||

document.documentElement.scrollTop>300){

topBtn.style.display="block";

}else{

topBtn.style.display="none";

}

}

function topFunction(){

window.scrollTo({

top:0,

behavior:"smooth"

});

}

/* Dark Mode */

let mode=document.querySelector(".mode");

let dark=false;

mode.onclick=function(){

if(!dark){

document.body.classList.add("dark");

mode.innerHTML="☀ Light";

dark=true;

}else{

document.body.classList.remove("dark");

mode.innerHTML="🌙 Dark";

dark=false;

}

}

/* Testimonials */

const names=[

"Rahul Sharma",

"Priya Reddy",

"Kiran Kumar",

"Aisha Khan",

"Ramesh Kumar"

];

const reviews=[

"Excellent doctors and friendly staff.",

"Very clean hospital and advanced facilities.",

"Emergency treatment was quick and professional.",

"I highly recommend CarePlus Hospital.",

"Doctors explained everything clearly and treated me well."

];

let i=0;

setInterval(function(){

i++;

if(i>=names.length){

i=0;

}

document.getElementById("patientName").innerHTML=names[i];

document.getElementById("patientReview").innerHTML=reviews[i];

},3000);

/* Counter Animation */

function counter(id,target){

let value=0;

let step=Math.ceil(target/150);

let timer=setInterval(function(){

value+=step;

if(value>=target){

value=target;

clearInterval(timer);

}

document.getElementById(id).innerHTML=value+"+";

},15);

}

counter("patients",15000);

counter("doctors",120);

counter("departments",40);

counter("awards",35);

counter("operations",9000);

</script>

</body>

</html>
"""

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True) 
    
