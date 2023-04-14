package me.reece.dojosandninjas.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import me.reece.dojosandninjas.models.Dojo;
import me.reece.dojosandninjas.repositories.DojoRepository;

@Service
public class DojoService {
	// adding the book repository as a dependency
    private final DojoRepository repo;
    
    public DojoService(DojoRepository repo) {
        this.repo = repo;
    }
    
    // returns all the books
    public List<Dojo> findAll() {
        return repo.findAll();
    }
    
    // creates a book
    public Dojo create(Dojo b) {
        return repo.save(b);
    }
    
    // retrieves a book
    public Dojo findOne(Long id) {
        Optional<Dojo> optional = repo.findById(id);
        if(optional.isPresent()) {
            return optional.get();
        } else {
            return null;
        }
    }
    
    public Dojo update(Dojo newObj) {
		Optional<Dojo> optional = repo.findById(newObj.getId());
		if(optional.isPresent()) {
			return repo.save(newObj);
		} else {
	    	return null;
		}
    }
    
    public void delete(Long id) {
		Optional<Dojo> optional = repo.findById(id);
		if(optional.isPresent()) {
			Dojo obj = optional.get();
			repo.delete(obj);
		}
    }
}