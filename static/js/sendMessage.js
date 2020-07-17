// Source : EmailJS API - https://www.emailjs.com/
// Send message function 
(function () {
    emailjs.init("user_GSvvZT0J6KvBUXPodOVCh");
})();

function sendMail(contactForm) {
    emailjs
        .send("gmail", "milestone3-20200717", {
            "type_of_request": contactForm.subject.value,
            "from_name" : contactForm.sender_name.value,
            "from_email": contactForm.email.value,
            "the_message": contactForm.messagetext.value
        })
        .then(
            function (response) {
                alert("Your message has been sent successfully.");
                $("#mail-form").get(0).reset();
            },
            function (error) {
                alert("Fail, please try again.");
            }
        );
    return false; // To block from loading a new page
}

$('#message-cancel').val('');
$('#message-cancel').next().removeClass('active');
