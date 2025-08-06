document.addEventListener("DOMContentLoaded", (event) => {
  const Form = document.getElementById("registration-form");
  const feedbackDiv = document.getElementById("form-feedback");
  const userName = document.getElementById("username");
  const userNameError = document.getElementById("usernameError");
  const email = document.getElementById("email");
  const emailError = document.getElementById("emailError");
  const password = document.getElementById("password");
  const passwordError = document.getElementById("passwordError");

  Form.addEventListener("submit", function (event) {
    event.preventDefault();
    const userNameInput = userName.value.trim();
    const emailInput = email.value.trim();
    const passwordInput = password.value.trim();
    let isValid = true;
    let messages = [];

    if (userNameInput.length < 3) {
      isValid = false;
      messages.push("Username should be at least 3 characters long");
      if (userNameError)
        userNameError.textContent =
          "Username should be at least 3 characters long";
    } else {
      if (userNameError) userNameError.textContent = "";
    }

    if (email.includes("!/^[w-]+(.[w-]+)*@([w-]+.)+[a-zA-Z]{2,7}$/")) {
      isValid = false;
      messages.push("Enter the correct form of email");
      if (emailError)
        emailError.textContent = "Enter the correct form of email";
    } else {
      if (emailError) emailError.textContent = "";
    }

    if (passwordInput.length < 8) {
      isValid = false;
      messages.push("Your password should be at least 8 characters");
      if (passwordError)
        passwordError.textContent =
          "Your password should be at least 8 characters";
    } else {
      if (passwordError) passwordError.textContent = "";
    }

    if (isValid) {
      if (feedbackDiv) {
        feedbackDiv.textContent = "Registration successful!";
        feedbackDiv.style.color = "#28a745";
      }
    } else {
      if (feedbackDiv) {
        feedbackDiv.textContent = messages.join(", ");
        feedbackDiv.style.color = "#dc3545";
      }
    }
  });
});
