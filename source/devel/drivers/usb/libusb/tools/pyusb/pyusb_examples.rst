
==============
pyusb examples
==============


Example1
========


:: 

	On Tue, Aug 24, 2010 at 3:43 PM, Max Teo <maxdaw@gmail.com> wrote:
	>    Surprisingly as I had mentioned previously in the comments above, using a
	> bus analyzer, the CSW status can be retrieved if I
	>    were to use another standalone Microsoft program to get the status back.
	>    What do you think could have caused this?
	>
	>   Something is preventing within this version that's preventing to read back
	> the CSW. I still think using lib-usb1.0 is a great start
	>   and would like to contribute back if I were to find anything.
	>
	>    Otherwise, what would you recommend?

I think libusb-1.0 should work if the other program works. 
A few suggestions:

- Post your pyusb program and Wander or others may point out whether
  your python pyusb code is correct or not.

- Enable debugging. libusb-1.0 Windows backend has the togglable
  debugging information (by calling libusb_set_debug(4)). pyusb should
  have similar things.

- Or you can directly use libusb-1.0 and C for testing purpose.

Since you have the bus analyzer, you can see the differences
on the wire.

Response
--------


I used both option 1 and 2 then :)

Its not even a program yet as its a trial to see if libusb can achieve 
what I desired.
Some snippets are cut out (not interesting and too much info)

:: 

	>>> import usb.core
	>>> import usb.util
	>>> import usb.backend.libusb10 as libusb10
	>>> backend = libusb10.get_backend()
	libusb:debug [libusb_init] created default context
	libusb:debug [libusb_init]
	libusb:debug [init_polling] Will use CancelIo for I/O cancellation
	libusb:debug [windows_clock_gettime_threaded] hires timer available (Frequency: 2000040000 Hz)
	libusb:debug [usbi_add_pollfd] add fd 3 events 1
	>>> backend
	<usb.backend.libusb10._LibUSB object at 0x01B2C4B0>
	>>> dev=usb.core.find(idVendor=0x152d, idProduct=0x2339, backend=backend)
	...
	libusb:debug [set_device_paths] path (3:2): \\.\USB#VID_152D&PID_2339#02000BFFFFFF#{A5DCBF10-6530-11
	D2-901F-00C04FB951ED}
	libusb:debug [set_device_paths] driver(s): WINUSB
	libusb:debug [set_device_paths] matched driver name against WinUSB API
	...

	>>> dev.set_configuration()
	libusb:debug [libusb_get_config_descriptor] index 0
	libusb:debug [libusb_open] open 3.2
	libusb:debug [libusb_set_configuration] configuration 1
	libusb:debug [libusb_claim_interface] interface 0
	libusb:debug [winusb_claim_interface] claimed interface 0
	libusb:debug [libusb_get_config_descriptor] index 0
	libusb:debug [windows_assign_endpoints] (re)assigned endpoint 81 to interface 0
	libusb:debug [windows_assign_endpoints] (re)assigned endpoint 02 to interface 0
	libusb:debug [auto_claim] auto-claimed interface 0 for control request
	libusb:debug [winusb_submit_control_transfer] will use interface 0
	libusb:debug [usbi_create_fd] could not duplicate handle for CancelIo - using original one
	libusb:debug [usbi_add_pollfd] add fd 4 events 1
	libusb:debug [libusb_get_next_timeout] next timeout in 0.991120s
	libusb:debug [handle_events] poll() 2 fds with timeout in 992ms
	libusb:debug [handle_events] poll() returned 1
	libusb:debug [windows_handle_events] checking fd 3 with revents = 0000
	libusb:debug [windows_handle_events] checking fd 4 with revents = 0001
	libusb:debug [usbi_remove_pollfd] remove fd 4
	libusb:debug [windows_transfer_callback] handling I/O completion with errcode 0
	libusb:debug [libusb_release_interface] interface 0
	libusb:debug [libusb_get_config_descriptor] index 0
	libusb:debug [windows_assign_endpoints] (re)assigned endpoint 81 to interface 0
	libusb:debug [windows_assign_endpoints] (re)assigned endpoint 02 to interface 0
	libusb:debug [auto_release] auto-released interface 0
	libusb:debug [ctrl_transfer_cb] actual_length=0

	>>> intf=dev.get_interface_altsetting()
	libusb:debug [libusb_get_config_descriptor] index 0
	>>> out = usb.util.find_descriptor(
	... intf, custom_match = \
	... lambda e: \
	... usb.util.endpoint_direction(e.bEndpointAddress) == \
	... usb.util.ENDPOINT_OUT)
	libusb:debug [libusb_get_config_descriptor] index 0
	>>> ind = usb.util.find_descriptor(
	... intf, custom_match = \
	... lambda e: \
	... usb.util.endpoint_direction(e.bEndpointAddress) == \
	... usb.util.ENDPOINT_IN)
	libusb:debug [libusb_get_config_descriptor] index 0
	libusb:debug [libusb_get_config_descriptor] index 0

	#  The commands below are trusted out commands; technically, if another session is sent out again
	# it will cause an abort reflected in the CSW.  As mentioned, the first command was sent out successfully, CSW was returned.

	>>> security_trusted_out = hex_digit_pairs_to_byte_array("55:53:42:43:11:34:66:78:00:02:00:00:80:00:
	0F:85:16:03:00:01:00:01:00:00:00:FE:00:07:00:5F:00", ":")
	>>> out.write(security_trusted_out)
	libusb:debug [libusb_get_config_descriptor] index 0
	libusb:debug [libusb_claim_interface] interface 0
	libusb:debug [winusb_claim_interface] claimed interface 0
	libusb:debug [libusb_get_config_descriptor] index 0
	libusb:debug [windows_assign_endpoints] (re)assigned endpoint 81 to interface 0
	libusb:debug [windows_assign_endpoints] (re)assigned endpoint 02 to interface 0
	libusb:debug [winusb_submit_bulk_transfer] matched endpoint 02 with interface 0
	libusb:debug [usbi_create_fd] could not duplicate handle for CancelIo - using original one
	libusb:debug [winusb_submit_bulk_transfer] writing 31 bytes
	libusb:debug [usbi_add_pollfd] add fd 4 events 4
	libusb:debug [libusb_get_next_timeout] next timeout in 0.990349s
	libusb:debug [handle_events] poll() 2 fds with timeout in 991ms
	libusb:debug [handle_events] poll() returned 1
	libusb:debug [windows_handle_events] checking fd 3 with revents = 0000
	libusb:debug [windows_handle_events] checking fd 4 with revents = 0004
	libusb:debug [usbi_remove_pollfd] remove fd 4
	libusb:debug [windows_transfer_callback] handling I/O completion with errcode 0
	libusb:debug [bulk_transfer_cb] actual_length=31

	>>> open_session = pad_blob_to_size(hex_digit_pairs_to_byte_array("00 00 00 00 07 FE 00 00 00 00 00
	00 00 00 00 00 00 00 00 50 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 38 0
	0 00 00 00 00 00 00 00 00 00 00 29 F8 A8 00 00 00 00 00 00 00 FF A8 00 00 00 00 00 00 FF 02 F0 83 01
	 2E 13 A8 00 00 02 05 00 00 00 01 01 F1 F9 F0 00 00 00 F1", " ").as_blob(), 512)

	>>> out.write(open_session)
	libusb:debug [libusb_get_config_descriptor] index 0
	libusb:debug [libusb_get_config_descriptor] index 0
	libusb:debug [winusb_submit_bulk_transfer] matched endpoint 02 with interface 0
	libusb:debug [usbi_create_fd] could not duplicate handle for CancelIo - using original one
	libusb:debug [winusb_submit_bulk_transfer] writing 512 bytes
	libusb:debug [usbi_add_pollfd] add fd 4 events 4
	libusb:debug [libusb_get_next_timeout] next timeout in 0.995021s
	libusb:debug [handle_events] poll() 2 fds with timeout in 996ms
	libusb:debug [handle_events] poll() returned 1
	libusb:debug [windows_handle_events] checking fd 3 with revents = 0000
	libusb:debug [windows_handle_events] checking fd 4 with revents = 0004
	libusb:debug [usbi_remove_pollfd] remove fd 4
	libusb:debug [windows_transfer_callback] handling I/O completion with errcode 0
	libusb:debug [bulk_transfer_cb] actual_length=512

	>>> ind.read(13, timeout=5000)
	libusb:debug [libusb_get_config_descriptor] index 0
	libusb:debug [libusb_get_config_descriptor] index 0
	libusb:debug [libusb_get_config_descriptor] index 0
	libusb:debug [libusb_get_config_descriptor] index 0
	libusb:debug [winusb_submit_bulk_transfer] matched endpoint 81 with interface 0
	libusb:debug [usbi_create_fd] could not duplicate handle for CancelIo - using original one
	libusb:debug [winusb_submit_bulk_transfer] reading 13 bytes
	libusb:debug [usbi_add_pollfd] add fd 4 events 1
	libusb:debug [libusb_get_next_timeout] next timeout in 4.990351s
	libusb:debug [handle_events] poll() 2 fds with timeout in 4991ms
	libusb:debug [handle_events] poll() returned 1
	libusb:debug [windows_handle_events] checking fd 3 with revents = 0000
	libusb:debug [windows_handle_events] checking fd 4 with revents = 0001
	libusb:debug [usbi_remove_pollfd] remove fd 4
	libusb:debug [windows_transfer_callback] handling I/O completion with errcode 0
	libusb:debug [bulk_transfer_cb] actual_length=13

	array('B', [85, 83, 66, 83, 17, 52, 102, 120, 0, 0, 0, 0, 0])   <--- this is important which is CSW (status)
	>>>

	# repeating with the same loop as above

	>>> security_trusted_out = hex_digit_pairs_to_byte_array("55:53:42:43:11:34:66:78:00:02:00:00:80:00:
	0F:85:16:03:00:01:00:01:00:00:00:FE:00:07:00:5F:00", ":")
	>>> out.write(security_trusted_out)
	libusb:debug [libusb_get_config_descriptor] index 0
	libusb:debug [libusb_get_config_descriptor] index 0
	libusb:debug [winusb_submit_bulk_transfer] matched endpoint 02 with interface 0
	libusb:debug [usbi_create_fd] could not duplicate handle for CancelIo - using original one
	libusb:debug [winusb_submit_bulk_transfer] writing 31 bytes
	libusb:debug [usbi_add_pollfd] add fd 4 events 4
	libusb:debug [libusb_get_next_timeout] next timeout in 0.999222s
	libusb:debug [handle_events] poll() 2 fds with timeout in 1000ms
	libusb:debug [handle_events] poll() returned 1
	libusb:debug [windows_handle_events] checking fd 3 with revents = 0000
	libusb:debug [windows_handle_events] checking fd 4 with revents = 0004
	libusb:debug [usbi_remove_pollfd] remove fd 4
	libusb:debug [windows_transfer_callback] handling I/O completion with errcode 0
	libusb:debug [bulk_transfer_cb] actual_length=31

	>>> open_session = pad_blob_to_size(hex_digit_pairs_to_byte_array("00 00 00 00 07 FE 00 00 00 00 00
	00 00 00 00 00 00 00 00 50 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 38 0
	0 00 00 00 00 00 00 00 00 00 00 29 F8 A8 00 00 00 00 00 00 00 FF A8 00 00 00 00 00 00 FF 02 F0 83 01
	 2E 13 A8 00 00 02 05 00 00 00 01 01 F1 F9 F0 00 00 00 F1", " ").as_blob(), 512)

	>>> out.write(open_session)
	libusb:debug [libusb_get_config_descriptor] index 0
	libusb:debug [libusb_get_config_descriptor] index 0
	libusb:debug [winusb_submit_bulk_transfer] matched endpoint 02 with interface 0
	libusb:debug [usbi_create_fd] could not duplicate handle for CancelIo - using original one
	libusb:debug [winusb_submit_bulk_transfer] writing 512 bytes
	libusb:debug [usbi_add_pollfd] add fd 4 events 4
	libusb:debug [libusb_get_next_timeout] next timeout in 0.999240s
	libusb:debug [handle_events] poll() 2 fds with timeout in 1000ms
	libusb:debug [handle_events] poll() returned 1
	libusb:debug [windows_handle_events] checking fd 3 with revents = 0000
	libusb:debug [windows_handle_events] checking fd 4 with revents = 0004
	libusb:debug [usbi_remove_pollfd] remove fd 4
	libusb:debug [windows_transfer_callback] handling I/O completion with errcode 0
	libusb:debug [bulk_transfer_cb] actual_length=512

	>>> ind.read(13, timeout=5000)
	libusb:debug [libusb_get_config_descriptor] index 0
	libusb:debug [libusb_get_config_descriptor] index 0
	libusb:debug [winusb_submit_bulk_transfer] matched endpoint 81 with interface 0
	libusb:debug [usbi_create_fd] could not duplicate handle for CancelIo - using original one
	libusb:debug [winusb_submit_bulk_transfer] reading 13 bytes
	libusb:debug [usbi_add_pollfd] add fd 4 events 1
	libusb:debug [libusb_get_next_timeout] next timeout in 4.999235s
	libusb:debug [handle_events] poll() 2 fds with timeout in 5000ms
	libusb:debug [handle_events] poll() returned 1
	libusb:debug [windows_handle_events] checking fd 3 with revents = 0000
	libusb:debug [windows_handle_events] checking fd 4 with revents = 0001
	libusb:debug [usbi_remove_pollfd] remove fd 4
	libusb:debug [windows_transfer_callback] handling I/O completion with errcode 31
	libusb:debug [windows_transfer_callback] detected endpoint stall
	libusb:debug [bulk_transfer_cb] actual_length=0
	Traceback (most recent call last):

	  File "<stdin>", line 1, in <module>
	  File "usb\core.py", line 273, in read
	  File "usb\core.py", line 624, in read
	  File "usb\_debug.py", line 53, in do_trace
	  File "C:\sandbox\openseapy\Kwai_Phase2_Internal_Review\toolbox\usb\backend\libusb10.py", line 483,
	 in bulk_read
		timeout)
	  File "C:\sandbox\openseapy\Kwai_Phase2_Internal_Review\toolbox\usb\backend\libusb10.py", line 581,
	 in __read
		timeout))
	  File "C:\sandbox\openseapy\Kwai_Phase2_Internal_Review\toolbox\usb\backend\libusb10.py", line 353,
	 in _check
		raise USBError(_str_error[retval.value])
	usb.core.USBError: Pipe error
	>>>

	I tried polling for a few times by sending a libusb_clear_halt,  
	(technically its not required for the other standalone program)
	but got back the Pipe error.


