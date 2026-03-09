import redirects from "../../redirects.json" assert { type: "json" };

export default async (request) => {
  const hostname = new URL(request.url).hostname;
  const target = redirects[hostname];

  if (target) {
    return Response.redirect(target, 302);
  }

  return new Response("Not found", { status: 404 });
};

export const config = { path: "/*" };
