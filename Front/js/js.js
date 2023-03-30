function log_in() {
    const form = document.getElementById('login-form');

    form.addEventListener('submit', async (event) => {
        event.preventDefault(); // prevent form submission
        const name = document.getElementById('name').value;
        const password = document.getElementById('password').value;

        const data = {"name": name, "password": password}; // create JavaScript object with form data

        const response = await fetch('/log-in', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data) // send form data as JSON
        });

        const responseData = await response.json(); // parse response data as JSON

        console.log(responseData); // do something with the response data
    });
}

function register() {
    const form = document.getElementById('register-form');

    form.addEventListener('submit', async (event) => {
        event.preventDefault(); // prevent form submission
        const name2 = document.getElementById('name2').value;
        const password2 = document.getElementById('password2').value;
        const password3 = document.getElementById('password3').value;
        const email = document.getElementById('email').value;

        const data = {"name": name2, "password": password2, "second_password": password3, "email": email}; // create JavaScript object with form data

        const response = await fetch('/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data) // send form data as JSON
        });

        const responseData = await response.json(); // parse response data as JSON

        console.log(responseData); // do something with the response data
    });
}

function contact() {
    const form = document.getElementById('contact');

    form.addEventListener('submit', async (event) => {
        event.preventDefault(); // prevent form submission
        const name = document.getElementById('esm').value;
        const email = document.getElementById('email2').value;
        const subject = document.getElementById('subject').value;
        const message = document.getElementById('message').value;

        const data = {"name": name, "subject": subject, "message": message, "email": email}; // create JavaScript object with form data

        const response = await fetch('/contact', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data) // send form data as JSON
        });

        const responseData = await response.json(); // parse response data as JSON

        console.log(responseData); // do something with the response data
    });
}