// Предполагаем, что у вас есть данные из формы, которые нужно передать на бэкенд 
const formData = { 
    fullname: 'fullname',
    date_time: 'DateOfBirth',
    pose: 'pose',
    curreet_pose: 'curreet_pose',
    offical_pose: 'offical_pose',
    phone: 'phone',
    email: 'email',
    spec: 'spec',
    data_work: 'data_work',
    region: 'region',
    

    email: 'myEmail@example.com' 
  }; 

  // Отправляем POST-запрос на URL вашего API 
  fetch('http://127.0.0.1:5000/DB', { 
    method: 'POST', // Указываем метод запроса 
    headers: { 
      'Content-Type': 'application/json' // Устанавливаем заголовок Content-Type для указания типа данных 
    }, 
    body: JSON.stringify(formData) // Преобразуем данные в формат JSON и передаем в теле запроса 
  }) 
  .then(response => { 
    if (!response.ok) { 
      throw new Error('Ошибка сети или сервера'); 
    } 
    return response.json(); // Парсим ответ сервера в формате JSON 
  }) 
  .then(data => { 
    console.log(data); // Обрабатываем полученные данные 
  }) 
  .catch(error => { 
    console.error(error); // Обрабатываем ошибки 
  });

