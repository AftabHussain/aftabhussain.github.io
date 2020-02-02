---
layout: page
title: SetUID is Bad
---

<small>Aftab Hussain <br><font color="gray">January 31, 2020</font>
<br><b><a href="../Tech-blog/index.html#unix-sys-admin"><small><i class="fa fa-tag" style="font-size:15px"></i>&nbsp;&nbsp;UNIX SYSTEM ADMINISTRATION</small></a></b></small>
<hr>

## **Let's get straight to the scenario**
<br>
If you leave your account open with another user for the time it takes to enter two bash commands, with the help of the setuid feature,
that user would have enough ability to compromise your entire account. 
Let's say your account is in a Unix server, and this other user also has an account in it.
And you are logged in. The other user sits in. Here's all he or she would need to do to take
total control of your account:

    $cp /bin/sh /tmp/mysh
    $chmod 4755 /tmp/mysh
    
The first copies the shell program to a commonly accessible `tmp` folder. The second makes the program a setUID program. Since 
the copy program is being created under your account, you own the program. Making it a setUID program allows it to be executed 
with your privileges, regardless of who runs it. Since it's put in the `tmp` directory, it could be run by anyone with an account
in the server. 

<hr>

## **What can we do?**
<br>
Apart from taking precautionary measures, like always logging out before leaving your computer, and checking your shell history
before sitting in, [disabling setuid](https://serverfault.com/a/547240) for parts of the file system is probably the safest way. You can read more about it from the
`mount` man page, and going over the `nosuid` option. 

I'm guessing due to the dangerous potential of the setuid bit, recent Unix distributions already prevent you from running script files 
with setuid functionality. As for binaries, they are still executable with setuid functionality. Check out this detailed [post](https://unix.stackexchange.com/a/2910) on this from 
Unix StackExchange.

<hr>

<b>Reference:</b>
<br><small>1. Computer Security Course by Prof. Wenliang (Kevin) Du, Syracuse University, New York</small>
