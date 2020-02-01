---
layout: page
title: The SetUID Motivation
---

<small>Aftab Hussain <br><font color="gray">January 30, 2020</font>
<br><b><a href="../Tech-blog/index.html#unix-sys-admin"><small><i class="fa fa-tag" style="font-size:15px"></i>&nbsp;&nbsp;UNIX SYSTEM ADMINISTRATION</small></a></b></small>
<hr>

## **SetUID programs in brief**
<br>
    
SetUID programs allow any user to run a program with the privileges of the owner of a program. 
You can create any program as a setUID program. 

Unix also has setUID programs on offer. These programs are owned by the root, and allow any 
user to run them with root privileges. 

Examples include `passwd` and `su`. (This `passwd` is the binary
which is found in the `/usr/bin/` folder. The one in the `/etc` folder is the configuration file which 
contains `passwd` information. `/etc` can contain other stuff too. Check [this](https://unix.stackexchange.com/a/56172) 
out on the (evolving) rationale of Unix's directory structure.) 

SetUID is useful, however as explained in a later post it can lead to security flaws. 
Now let's dive into this setUID business and see what's it all about, for real.

<hr>

## **What do SetUID programs look like, and how to create one?**
<br>

Any program can be a setUID program. Unix provides what is known as a setUID bit for 
any program. 

To realize the setUID<sup>1</sup> effect we would be dealing 
executable programs, which have the setUID bit set.

Recognizing a setUID program is easy in the shell GUI. They are highlighted, when 
listed with `ls -l`. Another, more sophisticated way of recognizing them is the
presence of `s` in their character-based permissions representation, also viewable with
`ls -l`:

    -rwsr-xr-x

The most accurate way to look at the status of the permission bits in my opinion is
just to check out their octal representation, as follows:

    $stat -c '%a' /tmp/
    $1777

For a setUID program the first octal digit would have a value of at least 4. 
To know why, take a look [here]().

<small> 1. I admit this word is already getting a bit repetitive, but
I can't think of a cuter synonym as of now, so I would need to stick to it. Sorry.</small>

### Creating a setUID program

Just use `chmod 4XYZ` (where XYZ are 3 octal digits). There are other ways, but this is the easiest.

<hr>

## **So how do setUID programs work?**
<br>

The key behind understanding the setUID mechanism is understanding who's in
charge of the setUID program, while the program is running.

So, let's backtrack a little bit, and ask ourselves how do we know who's in charge
of any running program? 

Before knowing this, it's important to understand that 
any running program is a process, and in UNIX every process has a set of 
information associated with them. We can obtain this information by viewing
this [file](https://superuser.com/a/1149434):

    $ /proc/<process-id>/status

Details about everything in this file can be found [here](http://man7.org/linux/man-pages/man5/proc.5.html).
For this discussion, the following are relevant:
    
> *the real user ID (real
uid, or ruid), the effective user ID (effective uid, or euid),
and the saved user ID (saved uid, or suid).* 
<br> *The **real uid** identifies the owner of the process.*
<br> *The **effective uid** is used in most access control decisions*
<br> *The **saved uid** stores a previous user ID so that it can be restored later.* 
<br> - Chen et al. (UC Berkeley, SRI International), [Setuid demystified](http://www.cs.umd.edu/~jkatz/TEACHING/comp_sec_F04/downloads/setuid.pdf), USENIX, 2002

Here's how the relevant line in the status file looks like, showing the above 3 values (we are mainly
concerned here with the first two):

> Uid:    1000    1000    1000    1000

The fourth number is the file system id, which is discussed [here](https://unix.stackexchange.com/a/45863).

The second number, the effective uid, is of most interest to us. This is the id 
based upon which various accesses are granted by the operating system.

### Getting process info with a setUID program in action

Now, let's run a UNIX setUID program, say `su`, from bash, and check out it's effective user id. 
After starting `su`, leave it running and open a new terminal. (To the best of my knowledge
once a process is closed, there are no traces of it, unless it has closed due to 
an error, in which case there's a log you can access.) 

Next, find the process id of the `su` process in any way you like. 
You can use `pstree -hp`, store it in a file if it is too big, and search there. 

Then show the status of the process using it's process id, using the method shown earlier.
You'll see:

> Uid:    1000    0    0    0

The effective userid of the process running `su` is 0 (the id of the 
owner of the program; that owner is root).

Now what about the userid of the process that called `su`. That process is the one running bash. We can
similarly find Uid information for this process as shown below:

> Uid:    1000    1000    1000    1000

This little experiment tells us a lot about how setuid programs work. A setuid program in execution
uses the permissions of the owner of the program to do its job. It does not use the permissions of the
owner of the process that called the setuid program, unless of course the owner of that calling process 
and the setuid program are the same. (For example a process owned by root calling `su`).

<hr>

## **Why have setuid?**
<br>

It allows users to carry out necessary functionalities without giving them total control over how to do it. 
`su` is one example. `/usr/bin/passwd` is another.

`passwd` allows a user to change his/her password. As we know
all passwords are stored in encrypted form in the `/etc/shadow` file. But if a user is allowed to change it, 
wouldn't this be a breach of security? If we don't, how do we change the password? [Prof. Kevin Du](http://www.cis.syr.edu/~wedu/) 
calls this the "password dilemma". The trick is to use a program trusted by the root to do the change. The user
is only able to invoke this program, not how it carries out the job.









