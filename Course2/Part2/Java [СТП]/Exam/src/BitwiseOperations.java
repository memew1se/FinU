import javax.swing.*;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/**
 * Класс для создания содержимого приложения и работы с побитовыми операциями
 */
public class BitwiseOperations extends JFrame implements ActionListener {

    Container container = getContentPane();
    String[] methods = {"&", "|", "^", "<<", ">>"};

    JTextField aTextField = new JTextField();
    JTextField bTextField = new JTextField();
    JTextField negationTextField = new JTextField();

    JLabel value = new JLabel("");
    JLabel quantity = new JLabel("");
    JLabel negationLabel = new JLabel("~");


    JButton abJButton = new JButton("Выполнить");
    JButton negationJButton = new JButton("Выполнить");
    JComboBox methodsComboBox = new JComboBox(methods);


    public BitwiseOperations() throws HeadlessException {
        setLayoutManager();
        setLocationAndSize();
        addActionEvent();
        addComponentsToContainer();
    }

    public void addActionEvent() {
        methodsComboBox.addActionListener(this);
        abJButton.addActionListener(this);
        negationJButton.addActionListener(this);
    }

    public void addComponentsToContainer() {
        container.add(methodsComboBox);
        container.add(aTextField);
        container.add(bTextField);
        container.add(abJButton);
        container.add(negationTextField);
        container.add(negationLabel);
        container.add(negationJButton);
        container.add(value);
        container.add(quantity);
    }

    public void setLayoutManager() {
        container.setLayout(null);
    }

    public void setLocationAndSize() {
        methodsComboBox.setBounds(165, 50, 70, 50);
        aTextField.setBounds(35, 65, 100, 20);
        bTextField.setBounds(265, 65, 100, 20);
        abJButton.setBounds(140, 115, 120, 20);
        value.setBounds(70, 40, 100, 20);
        quantity.setBounds(240, 40, 100, 20);
        negationTextField.setBounds(165, 150, 70, 20);
        negationLabel.setBounds(149, 150, 100, 20);
        negationJButton.setBounds(140, 180, 120, 20);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        try {
            if (e.getSource() == methodsComboBox){
                if (methodsComboBox.getSelectedItem() == "<<" || methodsComboBox.getSelectedItem() == ">>"){
                    value.setText("Значение");
                    quantity.setText("Количество");

                } else {
                    value.setText("");
                    quantity.setText("");
                }
            }

            else if (e.getSource() == abJButton) {
                if (!aTextField.getText().equals("") && !bTextField.getText().equals("")) {

                    int parseIntA = Integer.parseInt(aTextField.getText());
                    int parseIntB = Integer.parseInt(bTextField.getText());

                    String aBinary = Integer.toBinaryString(parseIntA);
                    String bBinary = Integer.toBinaryString(parseIntB);

                    String binary = "Входные данные: \n" + "В десятичной: " + parseIntA + ", в двоичной: " + aBinary + "\n" +
                            "В десятичной: " + parseIntB + ", в двоичной: " + bBinary + "\n" +
                            "\nРезультат: \n";

                    // Логическое и
                    if (methodsComboBox.getSelectedItem() == "&") {
                        int logicAnd = parseIntA & parseIntB;
                        //System.out.println("teeeeeeeeeeeeest");
                        JOptionPane.showMessageDialog(this,
                                binary + "В десятичной форме: "+
                                        Integer.toString(logicAnd) +
                                        "\nВ двоичной форме: " +
                                        Integer.toBinaryString(logicAnd),
                                "Результат", JOptionPane.INFORMATION_MESSAGE);
                        //System.out.println("2222222");

                        // логическое и
                    } else if (methodsComboBox.getSelectedItem() == "|") {
                        int logicOr = parseIntA | parseIntB;

                        JOptionPane.showMessageDialog(this,
                                binary +"В десятичной форме: "+
                                        Integer.toString(logicOr) +
                                        "\nВ двоичной форме: " +
                                        Integer.toBinaryString(logicOr),
                                "Результат", JOptionPane.INFORMATION_MESSAGE);

                        // Исключающее или
                    } else if (methodsComboBox.getSelectedItem() == "^") {
                        int exclOr = parseIntA ^ parseIntB;

                        JOptionPane.showMessageDialog(this,
                                binary + "В десятичной форме: "+
                                        Integer.toString(exclOr) +
                                        "\nВ двоичной форме: " +
                                        Integer.toBinaryString(exclOr),
                                "Результат", JOptionPane.INFORMATION_MESSAGE);

                        // Побитовый сдвиг влево
                    } else if (methodsComboBox.getSelectedItem() == "<<") {
                        int lShift = parseIntA << parseIntB;
                        JOptionPane.showMessageDialog(this,
                                "В десятичной форме: "+
                                        Integer.toString(lShift) +
                                        "\nВ двоичной форме: " +
                                        Integer.toBinaryString(lShift),
                                "Результат", JOptionPane.INFORMATION_MESSAGE);

                        // Побитовый сдвиг вправо
                    } else if (methodsComboBox.getSelectedItem() == ">>") {
                        int rShift = parseIntA >> parseIntB;

                        JOptionPane.showMessageDialog(this, "В десятичной форме: "+
                                Integer.toString(rShift) +
                                "\nВ двоичной форме: " +
                                Integer.toBinaryString(rShift),
                                "Результат", JOptionPane.INFORMATION_MESSAGE);
                    }
                }

                // Отрицание
            } else if (e.getSource() == negationJButton) {
                if (!negationTextField.getText().equals("")){

                    int parseNegation = Integer.parseInt(negationTextField.getText());
                    String binaryNegation = Integer.toBinaryString(parseNegation);

                    String binary = "Входные данные: \nВ десятичной: " + parseNegation + "\n" +
                            "В двоичной: " + binaryNegation + "\n" +
                            "\nРезультат: \n";

                    JOptionPane.showMessageDialog(this,
                            binary + "В десятичной форме: "+
                                    Integer.toString(~parseNegation) +
                                    "\nВ двоичной форме: " +
                                    Integer.toBinaryString(~parseNegation),
                            "Результат", JOptionPane.INFORMATION_MESSAGE);
                }
            }

        } catch (NumberFormatException exc) {
            JOptionPane.showMessageDialog(this, "Некорректно введены данные", "Ошибка", JOptionPane.ERROR_MESSAGE);
        }
    }
}
