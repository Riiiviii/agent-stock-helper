import { createRootRoute, Outlet } from "@tanstack/react-router";

export const Route = createRootRoute({
  component: () => (
    <>
      {/* TODO: replace placeholder landmarks with real navigation/footer */}
      <nav></nav>
      <Outlet />
      <footer />
    </>
  ),
});
