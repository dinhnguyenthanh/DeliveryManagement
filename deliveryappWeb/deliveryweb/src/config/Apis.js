import axios from 'axios'

export let endpoinds = {
    'categories': '/categories/'
}

export default axios.create({
    baseURL: "http://localhost:8000/"
})