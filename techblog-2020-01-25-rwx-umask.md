---
layout: page
title: Playing with permissions using umask & chmod
---

<small>Aftab Hussain <br><font color="gray">January 25, 2020</font>
<br><b><a href="../Tech-blog/index.html#unix-sys-admin"><small><i class="fa fa-tag" style="font-size:15px"></i>&nbsp;&nbsp;UNIX SYSTEM ADMINISTRATION</small></a></b></small>
<hr>

## **r, w, x**
<br>
Files and directories have permissions in UNIX, with respect to a user, a group, and others.

For example (output by `ll`),

    -rw-rw-r--  1 aftab aftab  74150 Jan 20 19:45 favicon1.ico
    
A total of 10 characters are used for determining a file's permission.
The first character is a dash, which shows that this is the information for a file. 

For a directory the first character would be a `d`. For example,

    drwxrwxr-x  2 aftab aftab   4096 Jan 20 18:57 css/

The next 9 characters show the permissions, of which the first 3 show the
access permissions for the file/directory available to a user. The next 3
characters show the access permissions available for the group. The last set of
3 characters show those available for anybody outside the group. 

(We can know the current user id, group, and all the available groups using `id`.)

Any 3-character set defines the following permissions, in the following order:
`read (r)`, `write (w)`, and `execute (x)`. The absence of these permissions is 
shown using a `-` in the corresponding position. 

For example, for the `favicon1.ico` file shown above, the user `aftab` 
does not have execute permissions.

<hr>

## **chmod**
<br>
The `chmod` command can be used to change the permissions of that file. Here's an example

    chmod 777 favicon1.ico

Each digit in the numeric input to chmod corresponds to a set of 3 characters
of the file's permission. As such, the characters are set based on the binary
representation of a digit. For example the first 7, is 111 in binary (by
converting each digit to its binary representation). This means the first 3
characters (or permissions) for the user would be changed to `rwx` (i.e. all
set). 777 gives maximum access to all users of a file.

<hr>

## **What about r, w, x for directories?**
<br>
`r` - You are able to see what's in a directory. 

`w` - You are able to write to a directory, i.e., create files and subfolders in it.

`x` - You can enter it, i.e., you can change directory into it, and access any of its files.

<small>Reference: 
<br> [File and Directory Permissions in UFS and NFS, MIT](http://web.mit.edu/sipb/doc/working/afs/html/subsection3.1.html)</small>

To know how to see octal permissions of a file, check out [How to get octal file permissions on Linux/Unix command line, nixCraft.](https://www.cyberciti.biz/faq/get-octal-file-permissions-from-command-line-on-linuxunix/)

<hr>

## **umask**
<br>
Unix defines something known as a default base permission or ***pre-defined initial permission*** which is generally 666. This gives us the following permissions,

    110110110 (in binary)
    rw-rw-rw- (in r,w,x character representation)

Now, when you create any file in UNIX, it is given a certain set of permissions
by default (the ***default permission***). Note that the above permissions are
**not** directly applied to the file. There is a little calculation that takes
place. 

A bit-wise AND is performed between the above pre-defined initial permission
(P) and the bit-wise OR of a ***umask permission*** (M). The result, the
default permission (R) 
of the file is obtained as follows:

    R = P & ( ! M )
    
Alternately, 

    R = P - M 
    (Using their octal representations)

Pre-defined initial permissions for files and directories are 666 and 777
respectively.  Default umask permissions for root user and the rest of the
users are 0022 and 0002 respectively.

<small>References: 
<br>[File Mode Creation Mask / umask Calculator](https://wintelguy.com/umask-calc.pl)
<br>[How to change Default Umask Permission in Linux, ComputerNetworkingNotes.com](https://www.computernetworkingnotes.com/rhce-study-guide/how-to-change-default-umask-permission-in-linux.html)

You can change the mask as follows:

    umask 0007

(Note the extra 0 in the beginning. This is because, by convention, UNIX represents these values using 4-bit octal numbers (0-7).)

<small>Reference: 
<br>[Practical Unix & Security](http://web.deu.edu.tr/doc/oreily/networking/puis/ch05_03.htm)</small>
    
## Example

Using the default settings, say we created a file `testfile.txt`. Here are the permission info:

    -rw-rw-r--
    
Let's see how we got the above. Since this is a file, the P value we would be
using is 666, and the M value is 002.  Subtracting, we get 664. This is
110110100 in binary (again, converting each digit to its binary
representation). Translating this binary sequence into the rwx-character
sequence gives us, `rw-rw-r--`.

<hr>

## **The Access Control List**
<br>
For more subtle management of permissions, we have something known as the access control list in Unix. 

> Access control list (ACL) provides an additional, more flexible permission mechanism for file systems. 
It is designed to assist with UNIX file permissions. ACL allows you to give 
permissions for any user or group to any disk resource. - [Access Control Lists, wiki.archlinux.org](https://wiki.archlinux.org/index.php/Access_Control_Lists)

`getfacl` (get full acl) and `setfacl` are the commands that would come handy. Check out the above link for details.





