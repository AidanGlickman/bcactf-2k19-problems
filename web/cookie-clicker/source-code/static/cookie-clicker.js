window.addEventListener("load", e => {
  // Lets store cookies as HTTP cookies!
  // Because they're cookies... see what I did there?

  const cookieCookie = document.cookie && document.cookie.split(";").map(cookie => cookie.split("=")).find(cookie => cookie[0].trim() === "cookies");
  cookies = cookieCookie && cookieCookie.length > 1 ? parseInt(cookieCookie[1]) : 0;

  const updateCookies = () => {
    document.querySelector(".counter *:first-child").innerText = cookies;
  };
  updateCookies();

  document.querySelector(".cookie").addEventListener("click", e => {
    const cookieCookie = document.cookie && document.cookie.split(";").map(cookie => cookie.split("=")).find(cookie => cookie[0].trim() === "cookies");
    if (cookieCookie && cookieCookie.length > 1 && !isNaN(parseInt(cookieCookie[1]))) {
      cookies = cookieCookie[1];
    }
    cookies++;
    document.cookie = `cookies=${cookies}`;
    updateCookies();
  });
});
