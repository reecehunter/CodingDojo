package me.reece.loginandregistration.controllers;

import java.util.Objects;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import jakarta.servlet.http.HttpSession;
import jakarta.validation.Valid;
import me.reece.loginandregistration.models.LoginUser;
import me.reece.loginandregistration.models.User;
import me.reece.loginandregistration.services.UserService;

@Controller
@RequestMapping("/users")
public class UserController {
	private final UserService userService;
	
	public UserController(UserService userService) {
		this.userService = userService;
	}
	
	@GetMapping("")
	public String loginReg(
			@ModelAttribute("newUser") User user,
			@ModelAttribute("loginUser") LoginUser loginUser) {
		return "/user/loginAndRegistration.jsp";
	}
	
	@PostMapping("/process/register")
	public String processRegisterUser(
			@Valid @ModelAttribute("newUser") User user,
			BindingResult result, Model model, HttpSession session) {
		// to-do - Reject values
		// reject if the password doesn't match
		if(!user.getPassword().equals(user.getConfirmPassword())) {
			result.rejectValue("password", "Match", "Passwords must match!");
		}
		// reject if the email is taken
		if(userService.getUser(user.getEmail()) != null) {
			result.rejectValue("email", "Unique", "Email is already taken!");
		}
		// re-render if errors
		if(result.hasErrors()) {
			model.addAttribute("loginUser", new LoginUser());
			return "user/loginAndRegistration.jsp";
		}
		User newUser = userService.registerUser(user);
		session.setAttribute("user_id", newUser.getId());
		return "redirect:/users/profile";
	}
	
	@PostMapping("/process/login")
	public String processLoginUser(@Valid @ModelAttribute("loginUser") LoginUser loginUser, BindingResult result, Model model, HttpSession session) {
		User loggingUser = userService.login(loginUser,result);
		if(result.hasErrors()) {
			model.addAttribute("newUser", new User());
			return "user/loginAndRegistration.jsp";
		}
		session.setAttribute("user_id", loggingUser.getId());
		return "redirect:/users/profile";
	}
	
	@GetMapping("/profile")
	public String profile(Model model, HttpSession session) {
		final long id = (long) session.getAttribute("user_id");
		if(Objects.isNull(id)) {
			return "redirect:/users";
		}
		final User user = userService.getUser(id);
		model.addAttribute("user", user);
		return "/user/profile.jsp";
	}
	
	@GetMapping("/logout")
	public String logout(HttpSession session) {
		session.invalidate();
		return "redirect:/users";
	}

}
