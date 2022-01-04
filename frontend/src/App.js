import { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [tasks, setTasks] = useState([])

  useEffect(() => {
    const apiURL = 'http://127.0.0.1:8000/api/'
    console.log("aaa");
    console.log(apiURL);
    fetch(`${apiURL}task/`)
      .then(data => data.json())
      .then(res => {
        setTasks(res)
      })
  }, [setTasks])
  return (
    <>
      <ul>
        {tasks.map(task => (
          <li key={task.id}>{task.name}</li>
        ))}
      </ul>
    </>
  );
}

export default App;
