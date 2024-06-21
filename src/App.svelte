<script>


    let correo = '';
    let clave = ' ';
    let mensaje ='';

async function login() {
        const response = await fetch('http://localhost:5000/registro_cliente/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ correo, clave })
        });

        const data = await response.json();
        mensaje = data.mensaje;
    }
</script>

<main>
	<h1>Login</h1>
    <input type="email" placeholder="Correo" bind:value={correo} />
    <input type="password" placeholder="clave" bind:value={clave}/>
    <button on:click={login}>Iniciar Sesión</button>
    <p>{mensaje}</p>
</main>

<style>
	
</style>