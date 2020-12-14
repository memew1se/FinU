package wikimedia;

import java.io.BufferedReader;
import java.io.InputStreamReader;

import java.net.HttpURLConnection;
import java.net.URL;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import java.util.*;

public class Parser {

    public Parser(String target) throws Exception {
        URL url = new URL("https://ru.wikipedia.org/w/api.php?" +
                "format=json&action=query&prop=extracts&explaintext=&exintro=&titles=" + target);
        HttpURLConnection httpURLConnection = (HttpURLConnection)url.openConnection();

        BufferedReader in = new BufferedReader(new InputStreamReader(httpURLConnection.getInputStream()));
        String response = in.readLine();
        in.close();

        Object obj = new JSONParser().parse(response);
        JSONObject jo = (JSONObject) obj;


        jo = (JSONObject) jo.get("query");
        jo = (JSONObject) jo.get("pages");
        Map map = (Map) jo;

        for (Object key : map.keySet()) {

            String k = key.toString();

            if (k.matches("(0|[1-9]\\d*)") == true) {
                Map valueMap = (Map) map.get(key);

                for (Object vkey : valueMap.keySet()) {
                    String vk = vkey.toString();

                    if (vk.equals("extract")) {
                        String answer = valueMap.get(vkey).toString();
                        answer = answer.replaceAll("\\p{Pd}", "-");

                        System.out.println("Вот что нашлось по запросу " + target + ":\n");
                        String[] sentences = answer.split("\\.");
                        for (String sentence : sentences) {
                            System.out.println(sentence);
                        }
                    }
                }

            } else {
                System.out.println("По запросу " + target + " ничего не нашлось");
            }
        }

    }


}


