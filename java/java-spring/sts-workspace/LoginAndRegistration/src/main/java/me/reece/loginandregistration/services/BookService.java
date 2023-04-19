package me.reece.loginandregistration.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;
import me.reece.loginandregistration.models.Book;
import me.reece.loginandregistration.repositories.BookRepository;

@Service
public class BookService {
	private final BookRepository repo;
	
	public BookService(BookRepository repo) {
		this.repo = repo;
	}
	
	public Book createOne(Book book) {
		return repo.save(book);
	}
	
	public Book getOne(Long id) {
		Optional<Book> potential = repo.findById(id);
		return potential.isPresent() ? potential.get(): null;
	}
	
	public List<Book> getAll() {
		return repo.findAll();
	}
    
    public Book update(Book book) {
		Optional<Book> optional = repo.findById(book.getId());
		if(optional.isPresent()) {
			return repo.save(book);
		} else {
	    	return null;
		}
    }
    
    public void delete(Long id) {
		Optional<Book> optional = repo.findById(id);
		if(optional.isPresent()) {
			Book book = optional.get();
			repo.delete(book);
		}
    }

}