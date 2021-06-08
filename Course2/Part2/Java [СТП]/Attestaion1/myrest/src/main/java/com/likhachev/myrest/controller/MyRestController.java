package com.likhachev.myrest.controller;

import com.likhachev.myrest.entity.Category;
import com.likhachev.myrest.entity.Task;
import com.likhachev.myrest.entity.User;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MyRestController {
    public static class RestResponse{
        private User user;
        private Task task;
        private Category category;

        public void setUser(User user) {
            this.user = user;
        }

        public void setTask(Task task) {
            this.task = task;
        }

        public void setCategory(Category category) {
            this.category = category;
        }
    }

    @RequestMapping(value = "/setAll", method = RequestMethod.GET,
            produces = MediaType.APPLICATION_JSON_VALUE)
    public RestResponse restMethod(User user, Task task, Category category) {
        RestResponse result = new RestResponse();
        result.setUser(user);
        result.setTask(task);
        result.setCategory(category);

        return result;
    }
}
