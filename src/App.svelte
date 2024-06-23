<script>
    import { Router, Route } from 'svelte-routing';
    import Login from '.Login.svelte'
</script>

<Router>
    <Route path="/" component={Login} />
</Router>
