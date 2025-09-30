/* 
**************************
MAKING THE ACCORDION WORK
**************************
*/

const div_service_description = document.querySelectorAll(
  ".service_description"
);
const div_service_header = document.querySelectorAll(".service_header");

div_service_header.forEach((header) => {
  header.addEventListener("click", () => {
    // Toggle the change_icon class on the header
    header.classList.toggle("change_icon");

    // Get the parent element of the header, which is the service_detail
    const service_detail = header.parentElement;
    const service_description = service_detail.querySelector(
      ".service_description"
    );

    // Toggle the active class on the service_description
    service_description.classList.toggle("active");

    // if (service_description.classList.contains("active"))
  });
});

/* 
**************************
ADDING A STICKY NAVBAR
**************************
*/
const section_hero_el = document.querySelector(".section-hero");
const obs = new IntersectionObserver(
  function (entries) {
    const ent = entries[0];
    console.log(ent);
    if (ent.isIntersecting == false) document.body.classList.add("sticky");

    if (ent.isIntersecting == true) document.body.classList.remove("sticky");
  },
  {
    // In the viewport
    root: null,
    threshold: 0,
    rootMargin: "-80px",
  }
);
obs.observe(section_hero_el);

///////////////////////////////////////////////////////////
// Smooth scrolling animation
const all_links = document.querySelectorAll(".main-header-link");
all_links.forEach(function (link) {
  link.addEventListener("click", function (e) {
    e.preventDefault();
    const href = link.getAttribute("href");

    // Scrool back to top
    if (href === "#")
      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });

    // Scroll to other links
    if (href !== "#" && href.startsWith("#")) {
      const section_el = document.querySelector(href);
      section_el.scrollIntoView({ behavior: "smooth" });
    }

    // Close mobile navigation
    if (link.classList.contains("main-nav-link"))
      headerEl.classList.toggle("nav-open");
  });
});

///////////////////////////////////////////////////////////
// Fixing flexbox gap property missing in some Safari versions
///////////////////////////////////////////////////////////

function checkFlexGap() {
  var flex = document.createElement("div");
  flex.style.display = "flex";
  flex.style.flexDirection = "column";
  flex.style.rowGap = "1px";

  flex.appendChild(document.createElement("div"));
  flex.appendChild(document.createElement("div"));

  document.body.appendChild(flex);
  var isSupported = flex.scrollHeight === 1;
  flex.parentNode.removeChild(flex);

  if (!isSupported) document.body.classList.add("no-flexbox-gap");
}
checkFlexGap();

///////////////////////////////////////////////////////////

// HOW TO MAKE THE NAVIGATION WORK
const btnNavEl = document.querySelector(".btn_mobile_nav");
const headerEl = document.querySelector(".main-header");

btnNavEl.addEventListener("click", function () {
  headerEl.classList.toggle("nav-open");
});

//  SHOW MAIL SUCCESS MESSAGE
const submitButton = document.querySelector(".btn_send");
const successMessage = document.querySelector(".success-message");

submitButton.addEventListener("click", function (e) {
  // setTimeout(function () {
  //   successMessage.style.display = "block";
  // }, 3000); // Show the message after 3 seconds
  console.log("clicked");
});
