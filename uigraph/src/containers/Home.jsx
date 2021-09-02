import React, {useEffect} from 'react';
import {Link} from 'react-router-dom';
import Typewriter from "typewriter-effect";
import '../styles/Home.css';

const Home = () =>{
    
    return (        
        <div>
            <div id="pulsating-circle1"/>
            <div id="pulsating-circle2"/>
            <div>
                <h1 className='typewrite'>
                    <Typewriter
                        options={{
                            loop:true,
                        }}
                        onInit={(typewriter) => {
                            typewriter
                                .start()
                                .typeString("Welcome to -Dash Now- platform!")
                                .pauseFor(2000)
                                .deleteAll()
                                .typeString("Your Custom Dashboard Step by Step.")
                                .pauseFor(2000)
                                .deleteAll()
                                .typeString("Easy to chart with lovely style.")
                                .pauseFor(2000)
                                .deleteAll()
                                .typeString("Security, KPIs, Alerts and much more!")
                                .pauseFor(2000)
                                .deleteAll()
                                .start();
                        }}
                    />
                </h1>
            </div>
                <Link to="/Login"><div id="testbutton"></div></Link>            
        </div>
     );
}

export default Home;

