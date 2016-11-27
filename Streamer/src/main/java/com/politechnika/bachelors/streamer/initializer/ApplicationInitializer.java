package com.politechnika.bachelors.streamer.initializer;


import com.politechnika.bachelors.streamer.datamodel.SingletonConfigModel;
import com.politechnika.bachelors.streamer.twitter.TwitterClientImpl;
import com.politechnika.bachelors.streamer.utils.input.InputParametersHandler;
import com.politechnika.bachelors.streamer.utils.input.InputParametersHolder;

import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * Created by Michau on 03.08.2016.
 */
public class ApplicationInitializer {
    private static final Logger log = Logger.getLogger(InputParametersHandler.class.getName());

    public static void main(String[] args) {
        SingletonConfigModel singletonConfigModel = SingletonConfigModel.getInstance();
        log.log(Level.INFO, "Config loaded");
        InputParametersHandler inputParametersHandler = new InputParametersHandler(args);
        InputParametersHolder inputParametersHolder = inputParametersHandler.getInputParameters();

        TwitterClientImpl twitterClient = TwitterClientImpl.getInstance();
        log.log(Level.INFO,"Preparing for streaming");
        twitterClient.prepareForStreaming(inputParametersHolder);
        log.log(Level.INFO,"Began streaming");
        twitterClient.startStreaming();

    }

}
