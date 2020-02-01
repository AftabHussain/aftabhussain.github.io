---
layout: page
title: The Unix way of storing passwords
---

<small>Aftab Hussain <br><font color="gray">January 26, 2020</font>
<br><b><a href="../Tech-blog/index.html#unix-sys-admin"><small><i class="fa fa-tag" style="font-size:15px"></i>&nbsp;&nbsp;UNIX SYSTEM ADMINISTRATION</small></a></b></small>
<hr>

## **The etc/passwd file**
<br>
This file stores the information for each user of a Unix operating system. Each user has a record dedicated to it. Here's an example.

    mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
    news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
    uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
    proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
    bob:x:1000:1000:bob,,,:/home/bob:/bin/bash

As we can see, there is an entry for user `bob`. The file consists of several columns (representing attributes), separated by colons. 
Each line has seven attributes. Let's see what each attribute means by looking at the entry for `bob`. 

    (1) bob : (2) x : (3) 1000 : (4) 1000 : (5) bob,,, : (6) /home/bob : (7) /bin/bash 
    (Spaces and numbers included for illustration purposes.)

Attribute 1 is the user name. The 2nd attribute is the password, which is a bit interesting:

> The password field originally contained an encrypted login password. However, for security reasons, the encrypted passwords are now contained on another file, /etc/shadow, that cannot be read by ordinary users. This field now merely contains the letter x to indicate that a password has been assigned to the user and is required for authentication. 
If this field is empty, the user can log in without a password. - [The
/etc/passwd file, linfo.com,  Bellevue Linux Users
Group](http://www.linfo.org/etc_passwd.html)
    
To know details about the `/etc/shadow` file, for instance, what attributes it
stores for each user, what algorithms are used to store the passwords, and
changing user passwords, checkout [Understanding the /etc/shadow file from
nixCraft](https://www.cyberciti.biz/faq/understanding-etcshadow-file/).

Moving on, the 3rd and 4th attributes are the userid and the groupid
respectively. To know more about these attributes, e.g., the range of number
ids allowed and the set of predefined ids, please see the above link. The 5th
attribute contains general information about the user usually not needed by the
system. The 6th attribute is the full path of the home directory of the user.
The 7th attribute is the full path of the default shell for the user.

<hr>

## **The /etc/group file**
<br>
This is the file where we store information about the users in different groups
in the operating system. A record structure similar to the passwd file is used.
To learn about the attributes in this file and different cool ways about
knowing your group information (e.g. listing all groups where a given user is a
member of) checkout [Understanding /etc/group File from
nixCraft](https://www.cyberciti.biz/faq/understanding-etcgroup-file/).

