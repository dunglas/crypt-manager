.\"                                      Hey, EMACS: -*- nroff -*-
.TH CONCEAL 1 "august 16, 2007"
.\" Some roff macros, for reference:
.\" .nh        disable hyphenation
.\" .hy        enable hyphenation
.\" .ad l      left justify
.\" .ad b      justify to both left and right margins
.\" .nf        disable filling
.\" .fi        enable filling
.\" .br        insert line break
.\" .sp <n>    insert n+1 empty lines
.\" for manpage-specific macros, see man(7)
.SH NAME
conceal \- an encrypted folder manager
.SH SYNOPSIS
.B conceal
.RI [ options ] " directory" ...
.br
.SH DESCRIPTION
This manual page documents briefly the
.B conceal
command.
.PP
.\" TeX users may be more comfortable with the \fB<whatever>\fP and
.\" \fI<whatever>\fP escape sequences to invode bold face and italics, 
.\" respectively.
.SH OPTIONS
These programs follow the usual GNU command line syntax, with long
options starting with two dashes (`-').
A summary of options is included below.
For a complete description, see conceal \-\-help.
.TP
.B \-h, \-\-help
Show summary of options.
.TP
.B \-\-version
Show version of program.
.TP
.B \-e DIRECTORY, \-\-encrypt=DIRECTORY
encrypt DIRECTORY
.TP
.B \-c DIRECTORY, \-\-close=DIRECTORY
close DIRECTORY
.TP
.B \-o DIRECTORY, \-\-open=DIRECTORY
open encrypted DIRECTORY
.TP
.B \-i IDLE, \-\-idle=IDLE 
automaticaly close after IDLE time
.TP
.B \-d DIRECTORY, \-\-decrypt=DIRECTORY
decrypt DIRECTORY
.TP
.B \-p DIRECTORY, \-\-change\-password=DIRECTORY
change the password of DIRECTORY
.TP
.B \-l, \-\-clean
Clean directories list
.TP
.B \-s, -\-stdin
Get input from stdin
.SH SEE ALSO
.BR encfs (1),
.br
.SH AUTHOR
conceal was written by Kévin Dunglas <dunglas@gmail.com>.
.PP
This manual page was written by Kévin Dunglas <dunglas@gmail.com>,
for the Debian project (but may be used by others).
