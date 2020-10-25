import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
    const [today, setToday] = useState(0);

    useEffect(() => {
        fetch('/v1/api/today')
            .then(res => res.json())
            .then(data => {
                setToday(data.today);
            });
    }, []);

    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <p>Today is {today}</p>
            </header>
        </div>
    );
}

export default App;
