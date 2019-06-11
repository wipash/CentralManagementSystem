package com.helloworld.demo;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import org.json.simple.JSONObject;


/**
 * HelloWorldController
 */
@Controller
public class HelloWorldController {
    
    @RequestMapping(value="/", method=RequestMethod.GET, produces="application/json")
    @ResponseBody
    public JSONObject helloWorld() {
        JSONObject hello = new JSONObject();
        hello.put("message", "Hello World!");
        return hello;
    }
    
}
