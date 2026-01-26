/*
Template Name: Lexa - Admin & Dashboard Template
Author: Themesbrand
Website: https://themesbrand.com/
Contact: themesbrand@gmail.com
File: Session Timeout
*/

$.sessionTimeout({
	keepAliveUrl: '/extras/extra-pages/blank_page',
	logoutButton:'Logout',
	logoutUrl: '/extras/authentication/pages_login',
	redirUrl: '/extras/authentication/lock_screen',
	warnAfter: 3000,
	redirAfter: 30000,
	countdownMessage: 'Redirecting in {timer} seconds.'
});