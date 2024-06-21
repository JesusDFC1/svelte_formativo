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
<div class="login-container">
    <form class="login-form" on:submit={handleSubmit}>
        <h2>Login</h2>
        <div class="form-control">
            <label for="email">Correo Electrónico:</label>
            <input type="email" id="email" bind:value={email} required>
        </div>
        <div class="form-control">
            <label for="password">Clave:</label>
            <input type="password" id="password" bind:value={password} required>
        </div>
        <button type="submit" class="login-button">Ingresar</button>
    </form>
</div>

<style>
.login-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #f0f0f0;
    }

    .login-form {
        background-color: #fff;
        padding: 2rem;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        width: 100%;
        max-width: 400px;
    }

    .login-form h2 {
        margin-bottom: 1rem;
        color: #333;
    }

    .form-control {
        margin-bottom: 1rem;
    }

    .form-control label {
        display: block;
        margin-bottom: 0.5rem;
        color: #555;
    }

    .form-control input {
        width: 100%;
        padding: 0.5rem;
        border: 1px solid #ccc;
        border-radius: 4px;
        font-size: 1rem;
    }

    .login-button {
        width: 100%;
        padding: 0.75rem;
        border: none;
        border-radius: 4px;
        background-color: #000000;
        color: #000000;
        font-size: 1rem;
        cursor: pointer;
    }

    .login-button:hover {
        background-color: #000000;
    }	
</style>
