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

<title>CarePlus Premium Hospital</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

<link rel="stylesheet"
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css">

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:'Poppins',sans-serif;
scroll-behavior:smooth;
}

body{

background:#eef7ff;
overflow-x:hidden;
color:#333;

}

/* Scroll Bar */

::-webkit-scrollbar{
width:10px;
}

::-webkit-scrollbar-thumb{

background:#00b4d8;
border-radius:20px;

}

::-webkit-scrollbar-track{

background:#dff6ff;

}

/* Floating Background */

body::before{

content:"";

position:fixed;

width:600px;
height:600px;

background:radial-gradient(circle,
rgba(0,180,216,.25),
transparent);

top:-250px;
right:-200px;

z-index:-2;

animation:move1 10s infinite alternate;

}

body::after{

content:"";

position:fixed;

width:650px;
height:650px;

background:radial-gradient(circle,
rgba(255,105,180,.18),
transparent);

bottom:-250px;
left:-200px;

z-index:-2;

animation:move2 12s infinite alternate;

}

@keyframes move1{

100%{

transform:translate(-120px,90px);

}

}

@keyframes move2{

100%{

transform:translate(120px,-80px);

}

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

z-index:999999;

animation:hideLoader 2s forwards;
animation-delay:2s;

}

.loader span{

width:90px;
height:90px;

border-radius:50%;

border:10px solid #caf0f8;

border-top:10px solid #0077b6;

animation:spin 1s linear infinite;

}

@keyframes spin{

100%{

transform:rotate(360deg);

}

}

@keyframes hideLoader{

100%{

opacity:0;
visibility:hidden;

}

}

/* Top Bar */

.topbar{

background:linear-gradient(90deg,#003566,#0077b6,#00b4d8);

padding:10px;

display:flex;

justify-content:center;

gap:40px;

flex-wrap:wrap;

color:white;

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

background:rgba(255,255,255,.9);

backdrop-filter:blur(15px);

box-shadow:0 10px 25px rgba(0,0,0,.1);

z-index:1000;

}

.logo{

font-size:34px;

font-weight:800;

background:linear-gradient(45deg,#0077ff,#00d4ff,#00d68f);

-webkit-background-clip:text;

-webkit-text-fill-color:transparent;

}

nav a{

text-decoration:none;

margin-left:20px;

color:#333;

font-weight:600;

transition:.3s;

position:relative;

}

nav a:hover{

color:#0077ff;

}

nav a::after{

content:"";

position:absolute;

left:0;
bottom:-5px;

width:0;

height:3px;

background:#00b4d8;

transition:.3s;

}

nav a:hover::after{

width:100%;

}

.mode{

background:linear-gradient(45deg,#7b2cbf,#ff4fa3);

color:white;

padding:10px 20px;

border-radius:30px;

cursor:pointer;

font-weight:600;

transition:.3s;

}

.mode:hover{

transform:scale(1.05);

}

/* Hero */

.hero{

height:100vh;

background:

linear-gradient(rgba(0,0,0,.55),
rgba(0,0,0,.55)),

url("https://images.unsplash.com/photo-1586773860418-d37222d8fce3?auto=format&fit=crop&w=1800&q=80");

background-size:cover;
background-position:center;

display:flex;

justify-content:center;
align-items:center;
flex-direction:column;

text-align:center;

padding:20px;

color:white;

animation:zoomHero 20s infinite alternate;

}

@keyframes zoomHero{

100%{

background-size:115%;

}

}

.hero h1{

font-size:72px;

font-weight:800;

animation:down 1s;

}

.hero p{

font-size:24px;

margin-top:20px;

max-width:900px;

animation:up 2s;

}

.hero-buttons{

display:flex;

gap:20px;

margin-top:40px;

flex-wrap:wrap;

justify-content:center;

}

.btn{

padding:18px 40px;

border-radius:50px;

font-size:18px;

text-decoration:none;

font-weight:700;

transition:.4s;

}

.primary{

background:#00d68f;

color:white;

}

.secondary{

background:white;

color:#333;

}

.btn:hover{

transform:translateY(-8px);

}

@keyframes down{

from{

opacity:0;

transform:translateY(-70px);

}

to{

opacity:1;

transform:translateY(0);

}

}

@keyframes up{

from{

opacity:0;

transform:translateY(70px);

}

to{

opacity:1;

transform:translateY(0);

}

}

/* Horizontal Slider */

.horizontal-wrapper{

overflow:hidden;

padding:70px 0;

background:white;

}

.horizontal-track{

display:flex;

gap:30px;

width:max-content;

animation:slide 40s linear infinite;

}

.slide-card{

width:320px;

padding:30px;

background:white;

border-radius:20px;

box-shadow:0 10px 25px rgba(0,0,0,.1);

text-align:center;

transition:.4s;

}

.slide-card:hover{

transform:translateY(-10px);

}

.slide-card i{

font-size:60px;

color:#0077ff;

margin-bottom:15px;

}

@keyframes slide{

0%{

transform:translateX(0);

}

100%{

transform:translateX(-50%);

}

}

/* Common */

.section-title{

font-size:46px;

text-align:center;

margin:80px 0 50px;

color:#003566;

font-weight:800;

}

.grid{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(280px,1fr));

gap:30px;

padding:20px 60px 60px;

}

.card{

background:white;

padding:30px;

border-radius:25px;

box-shadow:0 10px 25px rgba(0,0,0,.08);

transition:.4s;

text-align:center;

}

.card:hover{

transform:translateY(-10px);

box-shadow:0 20px 35px rgba(0,180,216,.25);

}

.card i{

font-size:60px;

margin-bottom:20px;

color:#0077ff;

}

.stats{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(200px,1fr));

gap:30px;

padding:70px;

background:linear-gradient(45deg,#0077b6,#00b4d8);

color:white;

text-align:center;

}

.stats h2{

font-size:55px;

}

.dark{

background:#121212;

color:white;

}

.dark .card{

background:#1f1f1f;

color:white;

}

.dark header{

background:#111;

}

.dark nav a{

color:white;

}

.dark .slide-card{

background:#1f1f1f;

color:white;

}

.dark .horizontal-wrapper{

background:#121212;

}

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

margin:12px;

}

.hero h1{

font-size:42px;

}

.hero p{

font-size:18px;

}

.grid{

padding:20px;

}

}

</style>

</head>

<body>

<div class="loader">
<span></span>
</div>

<div class="topbar">

<div><i class="fa-solid fa-phone"></i> +91 9876543210</div>

<div><i class="fa-solid fa-envelope"></i> careplus@hospital.com</div>

<div><i class="fa-solid fa-truck-medical"></i> 24×7 Emergency</div>

<div><i class="fa-solid fa-award"></i> NABH Accredited</div>

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

<a href="#gallery">Gallery</a>

<a href="#appointment">Appointment</a>

<a href="#contact">Contact</a>

</nav>

<div class="mode">
🌙 Dark
</div>

</header>

<section class="hero">

<h1>Advanced Healthcare For Everyone</h1>

<p>

World-Class Doctors • Smart Technology • 24×7 Emergency Care • Compassionate Treatment

</p>

<div class="hero-buttons">

<a href="#appointment" class="btn primary">
Book Appointment
</a>

<a href="#services" class="btn secondary">
Explore Services
</a>

</div>

</section>

<!-- ================= EMERGENCY STRIP ================= -->

<section style="
background:linear-gradient(90deg,#ff1744,#ff6d00);
color:white;
padding:18px;
display:flex;
justify-content:center;
align-items:center;
gap:60px;
flex-wrap:wrap;
font-weight:600;
font-size:18px;">

<div>🚑 Emergency : +91 9876543210</div>

<div>🏥 Open 24 × 7</div>

<div>❤️ 120+ Specialist Doctors</div>

<div>⚡ Ambulance Within 10 Minutes</div>

</section>


<!-- ================= HORIZONTAL SERVICES ================= -->

<h2 class="section-title" id="services">
Our Premium Services
</h2>

<div class="horizontal-wrapper">

<div class="horizontal-track">

<div class="slide-card">
<i class="fa-solid fa-heart-pulse"></i>
<h3>Cardiology</h3>
<p>
Advanced heart treatment with modern equipment.
</p>
</div>

<div class="slide-card">
<i class="fa-solid fa-brain"></i>
<h3>Neurology</h3>
<p>
Brain and nervous system specialists.
</p>
</div>

<div class="slide-card">
<i class="fa-solid fa-bone"></i>
<h3>Orthopedics</h3>
<p>
Joint replacement and bone surgery.
</p>
</div>

<div class="slide-card">
<i class="fa-solid fa-eye"></i>
<h3>Eye Care</h3>
<p>
Complete vision care and LASIK surgery.
</p>
</div>

<div class="slide-card">
<i class="fa-solid fa-tooth"></i>
<h3>Dental Care</h3>
<p>
Cosmetic dentistry and implants.
</p>
</div>

<div class="slide-card">
<i class="fa-solid fa-baby"></i>
<h3>Pediatrics</h3>
<p>
Healthcare for infants and children.
</p>
</div>

<div class="slide-card">
<i class="fa-solid fa-lungs"></i>
<h3>Pulmonology</h3>
<p>
Expert treatment for respiratory diseases.
</p>
</div>

<div class="slide-card">
<i class="fa-solid fa-user-doctor"></i>
<h3>General Medicine</h3>
<p>
Complete health diagnosis and treatment.
</p>
</div>


<!-- Duplicate cards for infinite scrolling -->

<div class="slide-card">
<i class="fa-solid fa-heart-pulse"></i>
<h3>Cardiology</h3>
<p>
Advanced heart treatment with modern equipment.
</p>
</div>

<div class="slide-card">
<i class="fa-solid fa-brain"></i>
<h3>Neurology</h3>
<p>
Brain and nervous system specialists.
</p>
</div>

<div class="slide-card">
<i class="fa-solid fa-bone"></i>
<h3>Orthopedics</h3>
<p>
Joint replacement and bone surgery.
</p>
</div>

<div class="slide-card">
<i class="fa-solid fa-eye"></i>
<h3>Eye Care</h3>
<p>
Complete vision care and LASIK surgery.
</p>
</div>

<div class="slide-card">
<i class="fa-solid fa-tooth"></i>
<h3>Dental Care</h3>
<p>
Cosmetic dentistry and implants.
</p>
</div>

<div class="slide-card">
<i class="fa-solid fa-baby"></i>
<h3>Pediatrics</h3>
<p>
Healthcare for infants and children.
</p>
</div>

<div class="slide-card">
<i class="fa-solid fa-lungs"></i>
<h3>Pulmonology</h3>
<p>
Expert treatment for respiratory diseases.
</p>
</div>

<div class="slide-card">
<i class="fa-solid fa-user-doctor"></i>
<h3>General Medicine</h3>
<p>
Complete health diagnosis and treatment.
</p>
</div>

</div>

</div>


<!-- ================= QUICK ACCESS ================= -->

<h2 class="section-title">
Quick Access
</h2>

<section class="grid">

<div class="card">

<i class="fa-solid fa-calendar-check"></i>

<h3>Book Appointment</h3>

<p>

Book appointments instantly with our specialists.

</p>

</div>

<div class="card">

<i class="fa-solid fa-flask"></i>

<h3>Lab Reports</h3>

<p>

Download pathology reports securely online.

</p>

</div>

<div class="card">

<i class="fa-solid fa-pills"></i>

<h3>Online Pharmacy</h3>

<p>

Order medicines with doorstep delivery.

</p>

</div>

<div class="card">

<i class="fa-solid fa-ambulance"></i>

<h3>Emergency</h3>

<p>

Call ambulance immediately with one click.

</p>

</div>

<div class="card">

<i class="fa-solid fa-file-medical"></i>

<h3>Medical Records</h3>

<p>

Secure patient history and prescriptions.

</p>

</div>

<div class="card">

<i class="fa-solid fa-shield-heart"></i>

<h3>Health Insurance</h3>

<p>

Cashless treatment with leading insurance companies.

</p>

</div>

</section>


<!-- ================= HOSPITAL STATS ================= -->

<section class="stats">

<div>

<h2 id="patients">

0

</h2>

<p>

Happy Patients

</p>

</div>

<div>

<h2 id="doctorCount">

0

</h2>

<p>

Doctors

</p>

</div>

<div>

<h2 id="departments">

0

</h2>

<p>

Departments

</p>

</div>

<div>

<h2 id="operations">

0

</h2>

<p>

Successful Surgeries

</p>

</div>

<div>

<h2 id="awards">

0

</h2>

<p>

Awards

</p>

</div>

</section>


<!-- ================= TRUST SECTION ================= -->

<h2 class="section-title">
Why Patients Trust Us
</h2>

<section class="grid">

<div class="card">

<i class="fa-solid fa-award"></i>

<h3>25+ Years Experience</h3>

<p>

Providing quality healthcare with experienced medical professionals.

</p>

</div>

<div class="card">

<i class="fa-solid fa-user-group"></i>

<h3>15,000+ Happy Patients</h3>

<p>

Thousands of successful treatments every year.

</p>

</div>

<div class="card">

<i class="fa-solid fa-microscope"></i>

<h3>Modern Equipment</h3>

<p>

MRI, CT Scan, Robotic Surgery and Smart ICU.

</p>

</div>

<div class="card">

<i class="fa-solid fa-clock"></i>

<h3>24 × 7 Support</h3>

<p>

Doctors, Pharmacy and Emergency Services available all day.

</p>

</div>

</section>

<!-- ===================================================== -->
<!--                PART 2 - PREMIUM SECTIONS              -->
<!-- ===================================================== -->

<h2 class="section-title" id="doctors">
Meet Our Specialists
</h2>

<div class="doctor-slider">

<div class="doctor-track">

<div class="doctor-card">
<img src="https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?auto=format&fit=crop&w=800&q=80">
<h3>Dr. John Smith</h3>
<p>Senior Cardiologist</p>
<span>★★★★★</span>
</div>

<div class="doctor-card">
<img src="https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=800&q=80">
<h3>Dr. Sarah Johnson</h3>
<p>Neurologist</p>
<span>★★★★★</span>
</div>

<div class="doctor-card">
<img src="https://images.unsplash.com/photo-1594824476967-48c8b964273f?auto=format&fit=crop&w=800&q=80">
<h3>Dr. David Lee</h3>
<p>Orthopedic Surgeon</p>
<span>★★★★★</span>
</div>

<div class="doctor-card">
<img src="https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&w=800&q=80">
<h3>Dr. Emily Brown</h3>
<p>Pediatrician</p>
<span>★★★★★</span>
</div>

<div class="doctor-card">
<img src="https://images.unsplash.com/photo-1582750433449-648ed127bb54?auto=format&fit=crop&w=800&q=80">
<h3>Dr. Michael Davis</h3>
<p>General Surgeon</p>
<span>★★★★★</span>
</div>

<!-- Duplicate for seamless animation -->

<div class="doctor-card">
<img src="https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?auto=format&fit=crop&w=800&q=80">
<h3>Dr. John Smith</h3>
<p>Senior Cardiologist</p>
<span>★★★★★</span>
</div>

<div class="doctor-card">
<img src="https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=800&q=80">
<h3>Dr. Sarah Johnson</h3>
<p>Neurologist</p>
<span>★★★★★</span>
</div>

</div>

</div>



<h2 class="section-title">
Our Departments
</h2>

<div class="flip-grid">

<div class="flip-card">

<div class="flip-inner">

<div class="flip-front">

❤️

<h3>Cardiology</h3>

</div>

<div class="flip-back">

Heart surgery<br>
ECG<br>
Angiography<br>
24×7 Specialists

</div>

</div>

</div>

<div class="flip-card">

<div class="flip-inner">

<div class="flip-front">

🧠

<h3>Neurology</h3>

</div>

<div class="flip-back">

Stroke Care<br>
Brain Surgery<br>
EEG<br>
Neuro ICU

</div>

</div>

</div>

<div class="flip-card">

<div class="flip-inner">

<div class="flip-front">

🦴

<h3>Orthopedics</h3>

</div>

<div class="flip-back">

Fracture Care<br>
Joint Replacement<br>
Sports Medicine

</div>

</div>

</div>

<div class="flip-card">

<div class="flip-inner">

<div class="flip-front">

👶

<h3>Pediatrics</h3>

</div>

<div class="flip-back">

Vaccination<br>
NICU<br>
Child Specialists

</div>

</div>

</div>

</div>



<h2 class="section-title">
Hospital Journey
</h2>

<div class="timeline">

<div class="timeline-item">
<div class="circle">1998</div>
<p>Hospital Founded</p>
</div>

<div class="timeline-item">
<div class="circle">2007</div>
<p>ICU Started</p>
</div>

<div class="timeline-item">
<div class="circle">2015</div>
<p>NABH Certified</p>
</div>

<div class="timeline-item">
<div class="circle">2022</div>
<p>Robotic Surgery</p>
</div>

<div class="timeline-item">
<div class="circle">2026</div>
<p>AI Healthcare</p>
</div>

</div>



<h2 class="section-title">
Hospital Gallery
</h2>

<div class="gallery">

<img src="https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?auto=format&fit=crop&w=800&q=80">

<img src="https://images.unsplash.com/photo-1538108149393-fbbd81895907?auto=format&fit=crop&w=800&q=80">

<img src="https://images.unsplash.com/photo-1576091160550-2173dba999ef?auto=format&fit=crop&w=800&q=80">

<img src="https://images.unsplash.com/photo-1580281657527-47f249e8f4df?auto=format&fit=crop&w=800&q=80">

<img src="https://images.unsplash.com/photo-1526256262350-7da7584cf5eb?auto=format&fit=crop&w=800&q=80">

<img src="https://images.unsplash.com/photo-1584982751601-97dcc096659c?auto=format&fit=crop&w=800&q=80">

</div>



<style>

/* Doctor Slider */

.doctor-slider{
overflow:hidden;
padding:20px;
}

.doctor-track{
display:flex;
width:max-content;
animation:doctorMove 35s linear infinite;
gap:25px;
}

@keyframes doctorMove{

0%{transform:translateX(0);}

100%{transform:translateX(-50%);}

}

.doctor-card{

width:260px;

background:white;

border-radius:20px;

overflow:hidden;

box-shadow:0 10px 25px rgba(0,0,0,.15);

text-align:center;

transition:.5s;

}

.doctor-card:hover{

transform:translateY(-15px) scale(1.05);

}

.doctor-card img{

width:100%;

height:280px;

object-fit:cover;

}

.doctor-card h3{

margin:15px 0 5px;

}

.doctor-card span{

display:block;

padding-bottom:20px;

color:orange;

font-size:22px;

}



/* Flip Cards */

.flip-grid{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(240px,1fr));

gap:35px;

padding:50px;

}

.flip-card{

height:260px;

perspective:1000px;

}

.flip-inner{

position:relative;

width:100%;

height:100%;

transition:1s;

transform-style:preserve-3d;

}

.flip-card:hover .flip-inner{

transform:rotateY(180deg);

}

.flip-front,

.flip-back{

position:absolute;

width:100%;

height:100%;

border-radius:20px;

display:flex;

flex-direction:column;

justify-content:center;

align-items:center;

backface-visibility:hidden;

}

.flip-front{

background:linear-gradient(135deg,#0077b6,#00b4d8);

color:white;

font-size:60px;

}

.flip-back{

background:white;

transform:rotateY(180deg);

box-shadow:0 8px 20px rgba(0,0,0,.15);

font-size:20px;

}



/* Timeline */

.timeline{

display:flex;

justify-content:space-evenly;

flex-wrap:wrap;

padding:60px;

}

.timeline-item{

text-align:center;

}

.circle{

width:90px;

height:90px;

border-radius:50%;

background:#0077b6;

color:white;

display:flex;

align-items:center;

justify-content:center;

font-size:22px;

font-weight:bold;

margin:auto;

margin-bottom:15px;

transition:.5s;

}

.circle:hover{

transform:scale(1.2) rotate(360deg);

background:#00c896;

}



/* Gallery */

.gallery{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(300px,1fr));

gap:20px;

padding:40px;

}

.gallery img{

width:100%;

height:260px;

object-fit:cover;

border-radius:20px;

transition:.6s;

}

.gallery img:hover{

transform:scale(1.08) rotate(2deg);

filter:brightness(1.1);

}

</style>
<!-- ===================================================== -->
<!--                PART 3 - SMART FEATURES                -->
<!-- ===================================================== -->

<h2 class="section-title">Health Calculator</h2>

<section class="calculator-box">

<div class="calc-card">

<h3>🧮 BMI Calculator</h3>

<input type="number" id="weight" placeholder="Weight (kg)">

<input type="number" id="height" placeholder="Height (cm)">

<button onclick="calculateBMI()">Calculate BMI</button>

<h2 id="bmiResult">--</h2>

</div>

<div class="calc-card">

<h3>❤️ Heart Rate Status</h3>

<input type="number" id="pulse" placeholder="Enter Pulse">

<button onclick="checkPulse()">Check</button>

<h2 id="pulseResult">--</h2>

</div>

</section>



<h2 class="section-title">
Hospital Live Status
</h2>

<div class="status-grid">

<div class="status-card">
<h1 id="beds">120</h1>
<p>Available Beds</p>
</div>

<div class="status-card">
<h1 id="queue">18</h1>
<p>Patients Waiting</p>
</div>

<div class="status-card">
<h1 id="ambulance">8</h1>
<p>Ambulances Ready</p>
</div>

<div class="status-card">
<h1 id="clock">00:00:00</h1>
<p>Current Time</p>
</div>

</div>



<h2 class="section-title">
Blood Bank Availability
</h2>

<div class="blood-grid">

<div class="blood-card">🅰️ A+ <span>22 Units</span></div>

<div class="blood-card">🅱️ B+ <span>15 Units</span></div>

<div class="blood-card">🅾️ O+ <span>31 Units</span></div>

<div class="blood-card">🆎 AB+ <span>9 Units</span></div>

<div class="blood-card">🅰️ A- <span>5 Units</span></div>

<div class="blood-card">🅱️ B- <span>4 Units</span></div>

<div class="blood-card">🅾️ O- <span>7 Units</span></div>

<div class="blood-card">🆎 AB- <span>3 Units</span></div>

</div>



<h2 class="section-title">
Health Tips
</h2>

<div class="tip-box">

<h2 id="tipText">

Drink at least 8 glasses of water every day.

</h2>

</div>



<h2 class="section-title">
Book Ambulance
</h2>

<div class="ambulance-box">

<input type="text" placeholder="Patient Name">

<input type="tel" placeholder="Phone Number">

<input type="text" placeholder="Location">

<button onclick="bookAmbulance()">

🚑 Book Ambulance

</button>

</div>



<style>

/* Calculator */

.calculator-box{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(350px,1fr));

gap:30px;

padding:40px;

}

.calc-card{

background:white;

padding:30px;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.15);

text-align:center;

}

.calc-card input{

width:100%;

padding:15px;

margin:10px 0;

border-radius:10px;

border:1px solid #ccc;

}

.calc-card button{

padding:15px 30px;

border:none;

background:#0077b6;

color:white;

border-radius:10px;

cursor:pointer;

margin-top:10px;

}



/* Status */

.status-grid{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:25px;

padding:40px;

}

.status-card{

background:linear-gradient(135deg,#0077b6,#00b4d8);

color:white;

padding:30px;

border-radius:20px;

text-align:center;

transition:.5s;

}

.status-card:hover{

transform:translateY(-12px);

}



/* Blood Bank */

.blood-grid{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(180px,1fr));

gap:20px;

padding:40px;

}

.blood-card{

background:white;

padding:30px;

border-radius:20px;

font-size:28px;

font-weight:bold;

text-align:center;

box-shadow:0 8px 20px rgba(0,0,0,.12);

}

.blood-card span{

display:block;

margin-top:15px;

font-size:20px;

color:#0077b6;

}



/* Tips */

.tip-box{

max-width:900px;

margin:auto;

padding:35px;

background:#caf0f8;

border-radius:20px;

text-align:center;

font-size:28px;

}



/* Ambulance */

.ambulance-box{

max-width:700px;

margin:auto;

display:flex;

flex-direction:column;

gap:20px;

padding:40px;

}

.ambulance-box input{

padding:15px;

border-radius:10px;

border:1px solid #ccc;

}

.ambulance-box button{

padding:18px;

background:red;

color:white;

border:none;

font-size:20px;

border-radius:10px;

cursor:pointer;

}

</style>



<script>

/* BMI */

function calculateBMI(){

let w=document.getElementById("weight").value;

let h=document.getElementById("height").value/100;

if(w==""||h==0){

return;

}

let bmi=(w/(h*h)).toFixed(1);

document.getElementById("bmiResult").innerHTML="BMI : "+bmi;

}



/* Pulse */

function checkPulse(){

let p=document.getElementById("pulse").value;

let text="Normal";

if(p<60) text="Low";

if(p>100) text="High";

document.getElementById("pulseResult").innerHTML=text;

}



/* Clock */

setInterval(function(){

let d=new Date();

document.getElementById("clock").innerHTML=d.toLocaleTimeString();

},1000);



/* Live Queue */

setInterval(function(){

let q=document.getElementById("queue");

let value=parseInt(q.innerHTML);

value=value+(Math.floor(Math.random()*3)-1);

if(value<5) value=5;

if(value>30) value=30;

q.innerHTML=value;

},4000);



/* Tips */

const tips=[

"Drink at least 8 glasses of water every day.",

"Walk 30 minutes daily for a healthy heart.",

"Sleep 7-8 hours every night.",

"Eat fresh fruits and vegetables.",

"Exercise regularly to stay fit.",

"Reduce sugar and salt intake."

];

let tip=0;

setInterval(function(){

tip=(tip+1)%tips.length;

document.getElementById("tipText").innerHTML=tips[tip];

},3500);



/* Ambulance */

function bookAmbulance(){

alert("🚑 Ambulance booked successfully!");

}

</script>

<!-- ===================================================== -->
<!--                PART 4 - PREMIUM EFFECTS               -->
<!-- ===================================================== -->

<!-- Scroll Progress -->

<div id="progressBar"></div>

<!-- Floating Notification -->

<div id="notify">

🎉  New Appointment Booked Successfully!

</div>

<!-- AI Assistant -->

<div id="chatButton">

🤖

</div>

<div id="chatBox">

<h3>CarePlus AI Assistant</h3>

<p>

Hello 👋<br><br>

How can I help you today?

</p>

<input type="text" placeholder="Ask your question...">

<button onclick="closeChat()">

Close

</button>

</div>



<!-- Donation -->

<h2 class="section-title">

Support Poor Patients

</h2>

<section class="donation">

<h3>

Your contribution can save lives.

</h3>

<button onclick="donate()">

❤️ Donate Now

</button>

</section>



<!-- Floating Social -->

<div class="social">

<a href="#">📘</a>

<a href="#">📸</a>

<a href="#">🐦</a>

<a href="#">▶</a>

</div>



<!-- Mouse Glow -->

<div id="cursorGlow"></div>



<!-- Wave Footer -->

<div class="wave">

<svg viewBox="0 0 1440 320">

<path fill="#0077b6"

fill-opacity="1"

d="M0,96L80,112C160,128,320,160,480,181.3C640,203,800,213,960,197.3C1120,181,1280,139,1360,117.3L1440,96L1440,320L0,320Z">

</path>

</svg>

</div>



<style>

/* Progress */

#progressBar{

position:fixed;

top:0;

left:0;

height:5px;

width:0%;

background:#00ff99;

z-index:99999;

}



/* Notification */

#notify{

position:fixed;

top:25px;

right:-350px;

background:#00c896;

color:white;

padding:18px 30px;

border-radius:10px;

font-size:18px;

box-shadow:0 10px 20px rgba(0,0,0,.3);

transition:.8s;

z-index:999;

}



/* Chat */

#chatButton{

position:fixed;

bottom:30px;

left:25px;

width:70px;

height:70px;

border-radius:50%;

background:#0077b6;

color:white;

display:flex;

justify-content:center;

align-items:center;

font-size:34px;

cursor:pointer;

box-shadow:0 8px 20px rgba(0,0,0,.3);

z-index:999;

}

#chatBox{

position:fixed;

bottom:120px;

left:25px;

width:300px;

background:white;

padding:20px;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.3);

display:none;

z-index:999;

}

#chatBox input{

width:100%;

padding:12px;

margin:15px 0;

border:1px solid #ccc;

border-radius:8px;

}

#chatBox button{

padding:12px 20px;

background:#0077b6;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}



/* Donation */

.donation{

margin:60px auto;

max-width:800px;

padding:50px;

text-align:center;

background:linear-gradient(135deg,#0077b6,#00c896);

border-radius:25px;

color:white;

}

.donation button{

margin-top:20px;

padding:18px 40px;

font-size:20px;

border:none;

border-radius:40px;

background:white;

color:#0077b6;

cursor:pointer;

}



/* Social */

.social{

position:fixed;

right:20px;

top:40%;

display:flex;

flex-direction:column;

gap:15px;

z-index:999;

}

.social a{

width:55px;

height:55px;

background:white;

border-radius:50%;

display:flex;

align-items:center;

justify-content:center;

text-decoration:none;

font-size:26px;

box-shadow:0 8px 20px rgba(0,0,0,.25);

transition:.4s;

}

.social a:hover{

transform:scale(1.2);

}



/* Glow */

#cursorGlow{

position:fixed;

width:180px;

height:180px;

border-radius:50%;

background:radial-gradient(circle,

rgba(0,180,216,.35),

transparent);

pointer-events:none;

transform:translate(-50%,-50%);

z-index:-1;

}



/* Animated Background */

body{

background-size:400% 400%;

animation:bgMove 20s infinite alternate;

}

@keyframes bgMove{

0%{

background-position:left;

}

100%{

background-position:right;

}

}



/* Wave */

.wave svg{

display:block;

margin-top:-5px;

}

</style>



<script>

/* Scroll Progress */

window.addEventListener("scroll",function(){

let scroll=document.documentElement.scrollTop;

let height=document.documentElement.scrollHeight-

document.documentElement.clientHeight;

document.getElementById("progressBar").style.width=

(scroll/height)*100+"%";

});



/* Notification */

setTimeout(function(){

document.getElementById("notify").style.right="20px";

},4000);

setTimeout(function(){

document.getElementById("notify").style.right="-350px";

},9000);



/* Chat */

document.getElementById("chatButton").onclick=function(){

document.getElementById("chatBox").style.display="block";

}

function closeChat(){

document.getElementById("chatBox").style.display="none";

}



/* Glow */

document.addEventListener("mousemove",function(e){

let glow=document.getElementById("cursorGlow");

glow.style.left=e.clientX+"px";

glow.style.top=e.clientY+"px";

});



/* Donation */

function donate(){

alert("❤️ Thank you for supporting poor patients!");

}



/* Confetti Effect */

function confetti(){

for(let i=0;i<80;i++){

let c=document.createElement("div");

c.innerHTML="🎉";

c.style.position="fixed";

c.style.left=Math.random()*100+"vw";

c.style.top="-30px";

c.style.fontSize="30px";

c.style.transition="4s linear";

document.body.appendChild(c);

setTimeout(function(){

c.style.top="100vh";

},50);

setTimeout(function(){

c.remove();

},4200);

}

}



/* Connect with Appointment */

const oldBook=bookAppointment;

bookAppointment=function(e){

oldBook(e);

confetti();

}

</script>

</body>

</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
