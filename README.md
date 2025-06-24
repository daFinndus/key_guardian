# Key Guardian

You need strong passwords? This is the application for you!

![2](https://github.com/daFinndus/Key-Guardian/assets/128810466/f4185cd2-56d5-4127-90f3-07dcbbe019b2)

You can configure how many characters your password should contain or which type of characters! You can change the
application theme, use it in light- or dark mode or let your systems appearance decide.

### How can I install the application?

To install the application, clone the repository. After that go into the cloned repo, activate a virtual environment,
download the packages provided in the `requirements.txt` and execute main.py!

**NOTE**: You may have to install tkinter for your operating system too. Doing so is easy.

`sudo apt install python3-tk`

### How was the application built?

Everything was coded with Python, for the GUI I've used the custom tkinter library.

### How are you generating passwords?

Generating passwords may sound easy, but it isn't.
When using the normal "random" library of Python, which is created for game development or simulations, you might be
able to predict the pattern with which the random library creates your password.

So we are using the "secret" library, which is designed for cryptography. The difference is, it's way more updated and
doesn't use old patterns (MT19937).

### How's the strength meter working?

The strength meter checks your passwords entropy. There's a basic formula for that -> E = log2( R ^ L)

R is the amount of characters your password could contain, for example: It adds 26 characters when using only lowercase
letters. 26 more if you're also using uppercase letters. 10 more if you are using digits too and absolutely overkill: 34
more if you are using any symbols.

L is the length of your password.

The result will be in bits of entropy, a password is considered safe, when the bits of entropy are higher than 50.
A hacker which uses a brute-force attack to crack your password, let's say he can take 1 billion actions per second,
will need round about 560 seconds to crack a password with an entropy of 50 bits.

So choose a password that the hacker needs multiple billion years to crack! :)

Of course there's a lot more to a safe password, it shouldn't contain any words, or it shouldn't be used twice, there's
a
lot. Just use one Key Guardian Password per account and you'll be safe!

# First Version of Key Guardian

This is the first version of key guardian. It was just called password generator, and it wasn't working with a GUI yet,
you had to operate through the command prompt. You were able to configure the password length and which characters it
should contain, nothing more, nothing less.

![0](https://github.com/daFinndus/Key-Guardian/assets/128810466/cf10f972-8da7-47b0-9aad-af28eb01fe1d)

# The Update!

I've explored the tkinter library, which let's you create a GUI for your application. So I built it!
It kinda was a downgrade too, you weren't able to configure the length of your generated password anymore.

![1](https://github.com/daFinndus/Key-Guardian/assets/128810466/22d5f2d0-c87f-4569-8557-f8bba5a6f6f4)

# Final Product

This is the final product of Key Guardian. Now I am using the custom tkinter library, which makes all your elements look
way cleaner and adds some new stuff, like a slider! With a slider you were also able to change the length again, you
also have an option menu to change the theme of your application, make it light mode or dark mode. You get instant
feedback on how your password will be generated with which kinda character types. Also, there's the new strength
meter, an instant feedback on how strong your password is and how long it'll take a hacker to crack
it.

![2](https://github.com/daFinndus/Key-Guardian/assets/128810466/6c5a7f68-1a54-40f6-a084-67b16a2c3682)




