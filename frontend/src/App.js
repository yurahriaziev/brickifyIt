import './App.css';
import { Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import TestServer from './pages/ServerTest';

function App() {
  return (
    <div className="site">
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/server-test' element={<TestServer />} />
      </Routes>
    </div>
  )
}

export default App;
