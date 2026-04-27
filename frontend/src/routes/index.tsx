import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/")({
  component: RouteComponent,
});

function RouteComponent() {
  return (
    <div className="absolute inset-0 -z-10">
      <img
        className="object-cover w-full h-full"
        src="https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3"
        alt=""
      />
      <div className="absolute inset-0 bg-[#080e0c] opacity-94" />
    </div>
  );
}
