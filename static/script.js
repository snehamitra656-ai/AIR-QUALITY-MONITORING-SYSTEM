// ===============================
// Air Quality Monitoring System
// script.js
// ===============================

document.addEventListener("DOMContentLoaded", function () {

    console.log("Air Quality Monitoring System Loaded");

    // ===============================
    // Smooth Scroll
    // ===============================

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {

        anchor.addEventListener("click", function (e) {

            e.preventDefault();

            const target = document.querySelector(this.getAttribute("href"));

            if (target) {

                target.scrollIntoView({

                    behavior: "smooth"

                });

            }

        });

    });

    // ===============================
    // Predict Button Loading
    // ===============================

    const form = document.querySelector("form");
    const button = document.querySelector("button[type='submit']");

    if (form && button) {

        form.addEventListener("submit", function () {

            button.disabled = true;

            button.innerHTML =
                `<span class="spinner-border spinner-border-sm"></span> Predicting...`;

        });

    }

    // ===============================
    // Scroll Animation
    // ===============================

    const cards = document.querySelectorAll(".card");

    function revealCards() {

        const trigger = window.innerHeight * 0.90;

        cards.forEach(card => {

            const top = card.getBoundingClientRect().top;

            if (top < trigger) {

                card.style.opacity = "1";

                card.style.transform = "translateY(0px)";

            }

        });

    }

    cards.forEach(card => {

        card.style.opacity = "0";

        card.style.transform = "translateY(40px)";

        card.style.transition = "0.8s";

    });

    revealCards();

    window.addEventListener("scroll", revealCards);

    // ===============================
    // Scroll To Top Button
    // ===============================

    const topBtn = document.createElement("button");

    topBtn.innerHTML = "↑";

    topBtn.id = "topBtn";

    document.body.appendChild(topBtn);

    topBtn.style.position = "fixed";
    topBtn.style.right = "25px";
    topBtn.style.bottom = "25px";
    topBtn.style.width = "55px";
    topBtn.style.height = "55px";
    topBtn.style.borderRadius = "50%";
    topBtn.style.border = "none";
    topBtn.style.background = "#00c853";
    topBtn.style.color = "white";
    topBtn.style.fontSize = "25px";
    topBtn.style.cursor = "pointer";
    topBtn.style.display = "none";
    topBtn.style.boxShadow = "0 10px 20px rgba(0,0,0,.3)";
    topBtn.style.zIndex = "999";

    window.addEventListener("scroll", () => {

        if (window.scrollY > 300) {

            topBtn.style.display = "block";

        }

        else {

            topBtn.style.display = "none";

        }

    });

    topBtn.addEventListener("click", () => {

        window.scrollTo({

            top: 0,

            behavior: "smooth"

        });

    });

    // ===============================
    // Navbar Shadow
    // ===============================

    const navbar = document.querySelector(".navbar");

    window.addEventListener("scroll", () => {

        if (window.scrollY > 80) {

            navbar.style.background = "rgba(0,0,0,.65)";

            navbar.style.backdropFilter = "blur(18px)";

        }

        else {

            navbar.style.background = "rgba(0,0,0,.35)";

        }

    });

    // ===============================
    // Button Hover Animation
    // ===============================

    document.querySelectorAll(".btn").forEach(btn => {

        btn.addEventListener("mouseenter", () => {

            btn.style.transform = "scale(1.05)";

        });

        btn.addEventListener("mouseleave", () => {

            btn.style.transform = "scale(1)";

        });

    });

    // ===============================
    // Floating Dashboard Cards
    // ===============================

    document.querySelectorAll(".dashboard-card").forEach(card => {

        card.addEventListener("mouseenter", () => {

            card.style.transform = "translateY(-12px) scale(1.03)";

        });

        card.addEventListener("mouseleave", () => {

            card.style.transform = "translateY(0px)";

        });

    });

    // ===============================
    // AQI Result Animation
    // ===============================

    const result = document.querySelector(".display-3");

    if (result) {

        result.animate([

            {

                transform: "scale(.6)",

                opacity: 0

            },

            {

                transform: "scale(1)",

                opacity: 1

            }

        ],

        {

            duration: 1200

        });

    }

    // ===============================
    // Hero Image Floating
    // ===============================

    const heroImg = document.querySelector(".hero img");

    if (heroImg) {

        setInterval(() => {

            heroImg.style.transform = "translateY(-8px)";

            setTimeout(() => {

                heroImg.style.transform = "translateY(0px)";

            }, 1000);

        }, 2000);

    }

    // ===============================
    // Console Message
    // ===============================

    console.log("Developed using Flask + Machine Learning");

});