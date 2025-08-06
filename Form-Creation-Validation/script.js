document.addEventListener("DOMContentLoaded", (event) => {
  const Form = document.getElementById("registration-form");

  const feedbackDiv = document.getElementById("form-feedback");

  const form = document.addEventListener("submit", function (event) {
    event.preventDefault();
  });

  const userName = document.getElementById("username");
  const userNameError = document.getElementById("usernameError");
  const email = document.getElementById("email");
  const emailError = document.getElementById("emailError");
  const password = document.getElementById("password");
  const passwordError = document.getElementById("passwordError");

  const userNameInput = userName.value.trim();
  const emailInput = email.value.trim();
  const passwordInput = password.value.trim();

  let isValid = true;
  let messages = [console.error()];

  if (userNameInput.length < 3) {
    isValid = false;
    messages = "Usename should be at least 3 characters long";
  } else {
    console.log(userName.innerText);
  }
  if (!/^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/.test(emailInput)) {
    isValid = false;
    messages = "Enter the correct form of email";
  } else {
    console.log(email.innerText);
  }

  if (passwordInput.length < 8) {
    isValid = false;
    messages = "You passwaord should be atleast 8 characters";
  } else {
    console.log(password.innerText);
  }

  if (feedbackDiv) {
    isValid = true;
    feedbackDiv.textContent = "Registration successful!";
    feedbackDiv.style.color = "#28a745";
  }
});
