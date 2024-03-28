function sendData()
{
    var name = document.getElementById('nameInput').value;
    var email = document.getElementById('emailInput').value;
    var password = document.getElementById('passwordInput').value;



    document.querySelector('.name').innerHTML = `Name : ${name}`;
    document.querySelector('.email').innerHTML = `Email : ${email}`;
    document.querySelector('.password').innerHTML = `Password : ${password}`;

    window.location.href = "page2.html";

}
