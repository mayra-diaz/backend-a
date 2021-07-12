package data.dto;

public class UserDTO {
    private Long id;
    private String email;
    private String area;
    private String firstName;
    private String lastName;
    private String password;

    public UserDTO() {
    }

    public UserDTO(String email, String area) {
        this.email = email;
        this.area = area;
    }

    public UserDTO(String email, String area, String firstName, String lastName, String password) {
        this.email = email;
        this.area = area;
        this.firstName = firstName;
        this.lastName = lastName;
        this.password = password;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getArea() {
        return area;
    }

    public void setArea(String area) {
        this.area = area;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }


}

