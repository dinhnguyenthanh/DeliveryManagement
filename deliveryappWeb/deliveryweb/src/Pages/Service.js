import React, { useEffect, useState } from 'react'


const Service = () => {
    const [services, setService] = useState()

    useEffect(() => {
        let loadService = async() => {
            try{
                let res = await Apis.get(endpoints['service'])
                setService(res.data)
            } catch (err) {
            console.info(err)
            }
        }

        loadService()
    }, [])

    return (
        <div className='container'>
            <h1 className='text-center' style={{paddingTop: "20px"}}>Danh mục dịch vụ</h1>

            
        </div>
    )
}

export default Service