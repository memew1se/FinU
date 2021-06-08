import junit.framework.TestCase;
import org.junit.Assert;
import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

public class UserTest extends TestCase {

    @Test
    public void GetAllUsers(){
       User user = new User("Дмитрий",23, Sex.MALE);
       User user1 = new User("Елена",69, Sex.FAMALE);
       User user2 = new User("Вадим",41, Sex.MALE);
        List<User> actual = User.getAllUsers();

        List<User> expected = new ArrayList<>();
        expected.add(user);
        expected.add(user1);
        expected.add(user2);

        Assert.assertArrayEquals(expected, actual);
    }

    public void testGetAllUsers() {
    }

    public void testTestGetAllUsers() {
    }

    public void testGetHowManyUsers() {
    }

    public void testTestGetHowManyUsers() {
    }
}