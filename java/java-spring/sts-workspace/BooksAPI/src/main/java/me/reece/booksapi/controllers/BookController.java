package me.reece.booksapi.controllers;

import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

import me.reece.booksapi.models.Book;
import me.reece.booksapi.services.BookService;

@Controller
public class BookController {
    private final BookService bookService;
    
    public BookController(BookService bookService){
        this.bookService = bookService;
    }
	
	@GetMapping("/books")
	public String allBooks(Model model) {
		List<Book> books = bookService.allBooks();
		model.addAttribute("books", books);
		return "/books/showAll.jsp";
	}
	
	@GetMapping("/books/{id}")
	public String oneBook(
			@PathVariable("id") Long id,
			Model model) {
		Book book = bookService.findBook(id);
		model.addAttribute("book", book);
		return "/books/showOne.jsp";
	}

}
