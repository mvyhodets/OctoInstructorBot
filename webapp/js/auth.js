import {authUrl} from './config.js';

// Функция авторизации
async function authorize(token) {

// Запрос на авторизацию с токеном
const response = await fetch(authUrl, {
method: 'POST',
headers: {
'Content-Type': 'application/json'
},
body: JSON.stringify({token})
});

// Обработка результата
if(response.ok) {
const data = await response.json();
return {
user: data.user,
token: token
};
}

throw new Error('Authorization failed');

}

// Функция отправки данных боту
async function sendToBot(authResponse) {

// Создаем объект запроса
const response = await fetch('/bot/auth', {
method: 'POST',
headers: {
'Content-Type': 'application/json'
},
body: JSON.stringify(authResponse)
});

if(response.ok) {
return true;
}

throw new Error('Sending to bot failed');

}

// Экспортируем функцию
export async function authenticate(token) {
const authResponse = await authorize(token);
return sendToBot(authResponse);
}