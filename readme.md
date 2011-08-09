# Cafe Au Lait

This project is a fairly simple ordering system for a hypothetical coffee shop name _Cafe Au Lait_. The application is being designed for use on the Android mobile platform, as a webpage embedded into a webkit frame. The frontend makes heavy use of jQuery for the UI and for AJAX, with the backend being primarily a Python/Django & MySQL affair.

## JSON Data

![JSON Data](http://s.hzy.im/0645.jpg)

As shown in this screenshot, the current progress of the project is the frontend interface is able to take the values of all of the <input>'s on the order form, shove them into an array, and then JSONify them. This has it ready to be sent off via an AJAX request to Python where it can be placed in the database.