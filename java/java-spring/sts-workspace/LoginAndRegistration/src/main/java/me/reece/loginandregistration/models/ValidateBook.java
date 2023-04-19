package me.reece.loginandregistration.models;

import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;

public class ValidateBook {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @NotBlank(message="Title is required!")
    @Size(min=3, max=255, message="Username must be between 3 and 255 characters")
    private String title;
    
    @NotBlank(message="Author is required!")
    @Size(min=3, max=255, message="Author must be between 3 and 255 characters")
    private String author;
    
    @NotBlank(message="Your thoughts are required!")
    @Size(min=3, max=255, message="Your thoughts be at least 3 characters!")
    private String thoughts;
    
    
	public ValidateBook() {
		// TODO Auto-generated constructor stub
	}
	

	// Getters and setters
	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public String getAuthor() {
		return author;
	}

	public void setAuthor(String author) {
		this.author = author;
	}

	public String getThoughts() {
		return thoughts;
	}

	public void setThoughts(String thoughts) {
		this.thoughts = thoughts;
	}
	
}