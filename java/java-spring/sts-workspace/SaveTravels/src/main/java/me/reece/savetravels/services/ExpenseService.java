package me.reece.savetravels.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import me.reece.savetravels.models.Expense;
import me.reece.savetravels.repositories.ExpenseRepository;

@Service
public class ExpenseService {
	// adding the book repository as a dependency
    private final ExpenseRepository repo;
    
    public ExpenseService(ExpenseRepository repo) {
        this.repo = repo;
    }
    
    // returns all the books
    public List<Expense> findAll() {
        return repo.findAll();
    }
    
    // creates a book
    public Expense create(Expense b) {
        return repo.save(b);
    }
    
    // retrieves a book
    public Expense findOne(Long id) {
        Optional<Expense> optional = repo.findById(id);
        if(optional.isPresent()) {
            return optional.get();
        } else {
            return null;
        }
    }
    
    public Expense update(Expense burger) {
		Optional<Expense> optional = repo.findById(burger.getId());
		if(optional.isPresent()) {
			return repo.save(burger);
		} else {
	    	return null;
		}
    }
    
    public void delete(Long id) {
		Optional<Expense> optional = repo.findById(id);
		if(optional.isPresent()) {
			Expense expense = optional.get();
			repo.delete(expense);
		}
    }
}
