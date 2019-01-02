const config = require("./config.json");
const express = require("express");
const cookieParser = require("cookie-parser");
const path = require("path");

const app = express();
app.use(cookieParser());
app.use(express.static("static", {
  dotfiles: "ignore"
}));

app.set("view engine", "hbs");
app.set("views", "templates");

app.get("/flag", (req, res, next) => {
  if (req.cookies.cookies && req.cookies.cookies >= config.cookieThreshold) {
    res.type("text/plain").send(config.flag);
  } else {
    res.status(400).sendFile(path.join(__dirname, "static/notenoughcookies.html"));
  }
});

app.get("/shop", (req, res, next) => {
  res.render("shop", {
    cookies: req.cookies.cookies || 0,
    cookieThreshold: config.cookieThreshold
  });
});

app.listen(config.port);
