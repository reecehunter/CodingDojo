package me.reece.loginandregistration.repositories;

import java.util.List;
import java.util.Optional;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import me.reece.loginandregistration.models.Book;

@Repository
public interface BookRepository extends CrudRepository<Book, Long> {
	// get one
	Optional<Book> findById(Long id);
	// get all
	List<Book> findAll();

}