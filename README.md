# dump1090-fa Debian/Raspbian packages

This is a fork of [dump1090-mutability](https://github.com/mutability/dump1090)
customized for experimental use within Beaglebone and RTL-SDR. Use the make command

"make BLADERF=no"

(you may need to apt-get install libncurses5 to statisfy the curses dependency)

It is designed to build as a Debian package.


## Building manually

Just run "make" after installing the required dependencies.
Binaries are built in the source directory; you will need to arrange to
install them (and a method for starting them) yourself.

"make BLADERF=no" will disable bladeRF support and remove the dependency on
libbladeRF.

"make RTLSDR=no" will disable rtl-sdr support and remove the dependency on
librtlsdr.
