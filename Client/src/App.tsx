import { Provider } from 'react-redux'
import './App.css'
import { Login } from './pages/login'
import { store } from './redux/store'

function App() {


  return (
    <Provider store={store}>
      <Login />
    </Provider>
  )
}

export default App
