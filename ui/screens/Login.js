import React from 'react';
import { login, register } from '../services/service';

const Login = ({ setLoggedIn, loggedIn }) => {
    const [username, setUsername] = React.useState(null);
    const [password, setPassword] = React.useState(null);
    const loginToApp = () => {
        const data = {
            username: username,
            password: password
        };
        login(data)
            .then(res => {
                setLoggedIn(true);
            })
            .catch(err => {
                console.error(err);
            });
    };
    const onUsernameChange = (e) => {
        setUsername(e.target.value);
    };
    const onPasswordChange = (e) => {
        setPassword(e.target.value);
    };
    return (
        <div>
            {
                !loggedIn ?
                    <div style={{ display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center' }}>
                        <input onChange={onUsernameChange} style={{ textAlign: 'center' }} type="text" placeholder="username" />
                        <input onChange={onPasswordChange} style={{ textAlign: 'center' }} type="password" placeholder="password" />
                        <button onClick={loginToApp}>Login</button>
                    </div>
                :
                    <button onClick={() => setLoggedIn(false)}>Logout</button>
            }
        </div>
    )
};

export default Login;