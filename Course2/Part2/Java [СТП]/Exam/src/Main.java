import javax.swing.*;

/**
 * Приложение
 */
public class Main {
    public static void main(String[] args) {

        BitwiseOperations frame = new BitwiseOperations();
        frame.setTitle("Побитовые операции. Swing. Лихачев Марк ПИ19-3");
        frame.setVisible(true);

        // Если проблемы с отображением
        frame.setBounds(500, 300, 400, 280);

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setResizable(false);
    }
}
